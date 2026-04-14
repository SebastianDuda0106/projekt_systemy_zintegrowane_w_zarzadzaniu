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
        self.saveToXLS()

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

    def getTotalDemand(self,parent_demand=0):
        if parent_demand==0:temp_list = copy.deepcopy(self.parent_demand)
        else: temp_list = copy.deepcopy(parent_demand)
        for i in range(self.parent_assembly_time):
            temp_list.pop(0)
            temp_list.append(0)
        temp_list = [i * self.req_amount for i in temp_list]
        self.product_info.loc['Całkowite zapotrzebowanie'] = temp_list

    def calculate(self):
        last_week_order = 0
        total_required = self.product_info.loc['Całkowite zapotrzebowanie'].sum() - self.stock
        number_of_orders = math.ceil(int(total_required) / int(self.batch_size))

        for i in range(self.weeks, 1, -1):
            if(self.product_info.loc['Całkowite zapotrzebowanie',i] > 0):
                last_week_order = i
                break
        
        for i in range(number_of_orders):
            if(last_week_order - self.production_time > 0):
                self.product_info.loc['Planowane przyjęcie zamówień',last_week_order] = self.batch_size
                self.product_info.loc['Planowane zamówienia',last_week_order - self.production_time] = self.batch_size
                last_week_order -= self.production_time
            else:
                break


        self.product_info.loc['Przewidywane na stanie',1] = self.stock -self.product_info.loc['Całkowite zapotrzebowanie',1] 
        for i in range(1,self.weeks):
            self.product_info.loc['Przewidywane na stanie',i+1] = (
            self.product_info.loc['Planowane przyjęcie zamówień',i+1] 
            +self.product_info.loc['Przewidywane na stanie',i]
            -self.product_info.loc['Całkowite zapotrzebowanie',i+1]
            )
            if(self.product_info.loc['Przewidywane na stanie',i+1] < 0):
                self.product_info.loc['Zapotrzebowanie netto',i+1] = abs(self.product_info.loc['Przewidywane na stanie',i+1])

                
    def info(self):
        print(self.name)
        print(self.product_info)
        if self.req_amount > 1:
            print('Ilość w BOM                  ', self.req_amount,)
        print('\n')

    def saveToXLS(self):

        with pd.ExcelWriter(path=f'data.xlsx',mode='a',engine="openpyxl",if_sheet_exists="overlay") as writer:
            self.product_info.to_excel(writer, sheet_name=self.name)
            




    