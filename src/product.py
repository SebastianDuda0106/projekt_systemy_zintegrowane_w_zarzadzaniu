import numpy as np
import pandas as pd

class product:
    def __init__(self,production_time,production_amount,stock,req_amount,weeks):
        self.production_amount = production_amount
        self.production_time = production_time
        self.stock = stock
        self.req_amount = req_amount
        self.weeks = weeks
        self.createTable(weeks)
        self.product_info
        self.fillValues()
        self.calculateAvailable()


    def createTable(self, weeks):
        self.product_info = pd.DataFrame(np.zeros((3, weeks)))
        self.product_info = self.product_info.astype(int)
        self.product_info.index = [
            'Przewidywany popyt',
            'Produkcja',
            'Dostępne'
            ]
        self.product_info.columns +=1
        
    def fillValues(self):
        if(len(self.req_amount) == self.weeks):
            self.product_info.iloc[0] = self.req_amount
        else:
            print('wrong size of req_amount list')
        if(len(self.production_amount) == self.weeks):
            self.product_info.iloc[1] = self.production_amount
        else:
            print('wrong size of production_amount')

    def calculateAvailable(self):
        self.product_info.loc['Dostępne',1] = self.stock + self.product_info.loc['Produkcja',1] - self.product_info.loc['Przewidywany popyt',1] 
        for i in range(1,self.weeks):
            self.product_info.loc['Dostępne',i+1] = (
            self.product_info.loc['Produkcja',i+1] 
            +self.product_info.loc['Dostępne',i]
            -self.product_info.loc['Przewidywany popyt',i+1]
            )
    
    def getProductionTime(self):
        return self.production_time

    def getProduction(self):
        return self.production_amount
    
    def info(self):
        print(self.product_info)
        print('Czas realizacji    ' ,self.production_time)
        print('Na stanie          ' ,self.stock)