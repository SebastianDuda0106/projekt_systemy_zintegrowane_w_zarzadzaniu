import numpy as np
import pandas as pd

class product:
    def __init__(self,production_time,stock,req_amount,weeks):
        self.production_time = production_time
        self.stock = stock
        self.req_amount = req_amount
        self.weeks = weeks
        self.createTable(weeks)
        self.product_info
        self.fillRequiredAmount()


    def createTable(self, weeks):
        list = []
        for i in range(weeks):
            list.append(0)
        self.product_info = pd.DataFrame(np.zeros((3, weeks)))
        self.product_info = self.product_info.astype(int)
        self.product_info.index = [
            'Przewidywany popyt',
            'Produkcja',
            'Dostępne'
            ]
        
    def fillRequiredAmount(self):
        if(len(self.req_amount) == self.weeks):
            self.product_info.iloc[0] = self.req_amount
        else:
            print('wrong size of req_amount list')
    
    def info(self):
        print(self.product_info)
        print('Czas realizacji    ' ,self.production_time)
        print('Na stanie          ' ,self.stock)
        
        #self.product_info.loc['Przewidywany popyt',2] = 30
        #print(self.product_info.loc['Przewidywany popyt',2])