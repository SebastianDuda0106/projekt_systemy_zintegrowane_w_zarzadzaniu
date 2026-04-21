import numpy as np
import pandas as pd
import math
import copy
import xlsxwriter
import openpyxl

class component:
    def __init__(self,production_time,batch_size,BOM_level,stock,weeks,parent_assembly_time,parent_demand,name,req_amount=1):
        self.name = name
        self.production_time = production_time
        self.parent_assembly_time = parent_assembly_time
        self.batch_size = batch_size
        self.BOM_level = BOM_level
        self.stock = stock
        self.parent_demand = parent_demand
        self.weeks = weeks
        self.createTable(weeks)
        self.product_info
        self.req_amount = req_amount
        self.getTotalDemand()
        self.calculate()

    def createTable(self, weeks):
        list = []                                                   #CREATING DATAFRAME
        for i in range(weeks):
            list.append(0)
        self.product_info = pd.DataFrame(np.zeros((6, weeks)))      #FILLING WITH 0
        self.product_info = self.product_info.astype(int)
        self.product_info.index = [                                 #NAMING INDEXES
            'Całkowite zapotrzebowanie',
            'Planowane przyjęcia',
            'Przewidywane na stanie',
            'Zapotrzebowanie netto',
            'Planowane zamówienia',
            'Planowane przyjęcie zamówień'
        ]
        additional_info = pd.DataFrame([(self.production_time,self.batch_size,self.BOM_level,self.stock)]).transpose()
        additional_info.index = [
            'Czas realizacji',
            'Wielkość partii',
            'Poziom BOM',
            'Na stanie',
        ]
        self.product_info = pd.concat([self.product_info, additional_info])
        self.product_info.columns +=1
        self.product_info = self.product_info.replace({np.nan: ''})
        self.clearTable()


    def getTotalDemand(self,parent_demand=0):
        if parent_demand==0:temp_list = copy.deepcopy(self.parent_demand)
        else: temp_list = copy.deepcopy(parent_demand)
        for i in range(self.parent_assembly_time):
            temp_list.pop(0)
            temp_list.append(0)
        temp_list = [i * self.req_amount for i in temp_list]
        self.product_info.loc['Całkowite zapotrzebowanie'] = temp_list

    def calculate(self):
        current_order_week = 0 + self.production_time
        if current_order_week==0:   
            current_order_week += 1

        self.product_info.loc['Przewidywane na stanie',1] = self.stock -self.product_info.loc['Całkowite zapotrzebowanie',1] 
        for i in range(1,self.weeks):
            self.product_info.loc['Przewidywane na stanie',i+1] = ( 
            +self.product_info.loc['Przewidywane na stanie',i]
            +self.product_info.loc['Planowane przyjęcia', i+1]
            -self.product_info.loc['Całkowite zapotrzebowanie',i+1]
            )
            if(self.product_info.loc['Przewidywane na stanie',i+1] < 0):
                self.product_info.loc['Zapotrzebowanie netto',i+1] = abs(self.product_info.loc['Przewidywane na stanie',i+1])
            else:
                self.product_info.loc['Zapotrzebowanie netto',i+1] = 0
            if(self.product_info.loc['Zapotrzebowanie netto', i+1] > 0):
                if(current_order_week == i):
                    self.product_info.loc['Planowane przyjęcie zamówień', i+1] = self.batch_size
                    self.product_info.loc['Planowane zamówienia', i+1-self.production_time] = self.batch_size
                    current_order_week += self.production_time
                    self.product_info.loc['Przewidywane na stanie', i+1] += self.batch_size
            else:
                if(current_order_week == i):
                    self.product_info.loc['Planowane przyjęcie zamówień', i+1] = 0
                    self.product_info.loc['Planowane zamówienia', i+1-self.production_time] = 0
                    current_order_week += 1

    def clearTable(self):
        self.product_info[1:6] = 0

                
    def info(self):
        print(self.name)
        print(self.product_info)
        if self.req_amount > 1:
            print('Ilość w BOM                  ', self.req_amount,)
        print('\n')

    def saveToXLS(self, path='data.xlsx'):

        try:
            with pd.ExcelWriter(path=path,mode='a', engine="openpyxl",if_sheet_exists='overlay') as writer:
                self.product_info.to_excel(writer, sheet_name=self.name)
        except:
            with pd.ExcelWriter(path=path,mode='w', engine="openpyxl") as writer:
                self.product_info.to_excel(writer, sheet_name=self.name)

    def readXLS(self):
        self.product_info = pd.read_excel('data.xlsx', sheet_name=self.name, index_col=0, na_filter='')
            


    