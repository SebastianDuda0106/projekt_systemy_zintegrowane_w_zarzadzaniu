import numpy as np
import pandas as pd
from xml.dom import minidom
import os 
import xlsxwriter
import openpyxl


class product:
    def __init__(self,production_time,production_amount,stock,req_amount,weeks,name):
        self.name = name
        self.production_amount = production_amount
        self.production_time = production_time
        self.stock = stock
        self.req_amount = req_amount
        self.weeks = weeks
        self.createTable(weeks)
        self.product_info
        self.calculate()


    def createTable(self, weeks):
        ## CREATING DATAFRAME FOR MAIN PRODUCT AND FILLLING WITH 0
        self.product_info = pd.DataFrame(np.zeros((3, weeks)))
        self.product_info = self.product_info.astype(int)
        self.product_info.index = [
            'Przewidywany popyt',
            'Produkcja',
            'Dostępne'
            ]
        additional_info = pd.DataFrame([(self.production_time,self.stock)]).transpose()
        additional_info.index = [
            'Czas realizacji',
            'Na stanie',
        ]
        self.product_info = pd.concat([self.product_info, additional_info])
        self.product_info = self.product_info.replace({np.nan: ''})
        self.product_info.columns +=1

        ## FILLING DATAFRAME WITH DATA IF LENGTH OF LISTS ARE CORRECT
        if(len(self.req_amount) == self.weeks):
            self.product_info.iloc[0] = self.req_amount
        else:
            print('wrong size of req_amount list')
        if(len(self.production_amount) == self.weeks):
            self.product_info.iloc[1] = self.production_amount
        else:
            print('wrong size of production_amount')

        
    def calculate(self):
        ## CALCULATING AVAILABLE ROW BASED ON VALUES FROM WEEK BEFORE
        self.product_info.loc['Dostępne',1] = self.stock + self.product_info.loc['Produkcja',1] - self.product_info.loc['Przewidywany popyt',1] 
        for i in range(1,self.weeks):
            self.product_info.loc['Dostępne',i+1] = (
            self.product_info.loc['Produkcja',i+1] 
            +self.product_info.loc['Dostępne',i]
            -self.product_info.loc['Przewidywany popyt',i+1]
            )
    
    def info(self):
        ## DISPLAY INFO ABOUT PRODUCT
        print(self.name)
        print(self.product_info)

    def saveToXLS(self, path='data.xlsx'):
        try:
            with pd.ExcelWriter(path=path,mode='a', engine="openpyxl",if_sheet_exists='overlay') as writer:
                self.product_info.to_excel(writer, sheet_name=self.name)
        except:
            with pd.ExcelWriter(path=path,mode='w', engine="openpyxl") as writer:
                self.product_info.to_excel(writer, sheet_name=self.name)

    def readXLS(self, path='data.xlsx'):
        self.product_info = pd.read_excel(path, sheet_name=self.name, index_col=0, na_filter='')
        print(self.product_info)