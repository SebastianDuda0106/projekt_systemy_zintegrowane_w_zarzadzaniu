import numpy as np
import pandas as pd
import math

class component:
    def __init__(self,production_time,batch_size,BOM_level,stock,weeks,parent_assembly_time,parent_demand,req_amount=1):
        self.production_time = production_time
        self.parent_assembly_time = parent_assembly_time
        self.batch_size = batch_size
        self.BOM_level = BOM_level
        self.stock = stock
        self.parent_demand = parent_demand
        self.weeks = weeks
        print(self.weeks)
        self.createTable(weeks)
        self.product_info
        self.req_amount = req_amount
        self.getTotalDemand()
        self.calculate()

    def createTable(self, weeks):
        list = []
        for i in range(weeks):
            list.append(0)
        self.product_info = pd.DataFrame(np.zeros((6, weeks)))
        self.product_info = self.product_info.astype(int)
        self.product_info.index = [
            'Całkowite zapotrzebowanie',
            'Planowane przyjęcia',
            'Przewidywane na stanie',
            'Zapotrzebowanie netto',
            'Planowane zamówienia',
            'Planowane przyjęcie zamówień'
        ]
        self.product_info.columns +=1

    def getTotalDemand(self):
        print(self.parent_demand)
        for i in range(self.parent_assembly_time):
            self.parent_demand.pop(0)
            self.parent_demand.append(0)
        print(self.parent_demand)
        self.product_info.loc['Całkowite zapotrzebowanie'] = self.parent_demand
        self.info()


    def info(self):
        print(self.product_info)
        print('Czas realizacji              ', self.production_time)
        print('Wielkość partii              ', self.batch_size)
        print('Poziom BOM                   ', self.BOM_level)
        print('Na stanie                    ', self.stock)
        if self.req_amount > 1:
            print('Ilość w BOM                  ', self.req_amount)

    def calculate(self):
        last_week_order = 0
        total_required = self.product_info.loc['Całkowite zapotrzebowanie'].sum()
        print(total_required - self.stock)
        number_of_orders = math.ceil(int(total_required) / int(self.batch_size))

        for i in range(self.weeks, 1, -1):
            if(self.product_info.loc['Całkowite zapotrzebowanie',i] > 0):
                last_week_order = i
                break
        
        for i in range(number_of_orders):
            self.product_info.loc['Planowane przyjęcie zamówień',last_week_order] = self.batch_size
            self.product_info.loc['Planowane zamówienia',last_week_order - self.production_time] = self.batch_size
            last_week_order -= self.production_time


        self.product_info.loc['Przewidywane na stanie',1] = self.stock -self.product_info.loc['Całkowite zapotrzebowanie',1] 
        for i in range(1,self.weeks):
            self.product_info.loc['Przewidywane na stanie',i+1] = (
            self.product_info.loc['Planowane przyjęcie zamówień',i+1] 
            +self.product_info.loc['Przewidywane na stanie',i]
            -self.product_info.loc['Całkowite zapotrzebowanie',i+1]
            )
            if(self.product_info.loc['Przewidywane na stanie',i+1] < 0):
                self.product_info.loc['Zapotrzebowanie netto',i+1] = abs(self.product_info.loc['Przewidywane na stanie',i+1])
        self.info()





    