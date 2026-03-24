import numpy as np
import pandas as pd

class component:
    def __init__(self,production_time,batch_size,BOM_level,stock,weeks,parent_assembly_time,parent_demand,req_amount=1):
        self.production_time = production_time
        self.parent_assembly_time = parent_assembly_time
        self.batch_size = batch_size
        self.BOM_level = BOM_level
        self.stock = stock
        self.parent_demand = parent_demand
        self.weeks = weeks - parent_assembly_time
        self.createTable(weeks)
        self.product_info
        self.req_amount = req_amount

    def createTable(self, weeks):
        list = []
        for i in range(weeks):
            list.append(0)
        self.product_info = pd.DataFrame(np.zeros((6, weeks)))
        self.product_info.index = [
            'Całkowite zapotrzebowanie',
            'Planowane przyjęcia',
            'Przewidywane na stanie',
            'Zapotrzebowanie netto',
            'Planowane zamówienia',
            'Planowane przyjęcie zamówień'
        ]

    def getTotalDemand(self):
        for i in range(self.weeks):
            self.parent_demand.pop(0)
        self.product_info.loc['Całkowite zapotrzebowanie',0] = self.parent_demand
        self.info()


    def info(self):
        print(self.product_info,'\n')






    