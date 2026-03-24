import numpy as np
import pandas as pd

class component:
    def __init__(self,production_time,batch_size,BOM,stock,weeks,req_amount=1):
        self.production_time = production_time
        self.batch_size = batch_size
        self.BOM = BOM
        self.stock = stock
        self.createTable(weeks)
        self.product_info
        self.req_amount = req_amount

    def createTable(self, weeks):
        list = []
        for i in range(weeks):
            list.append(0)
        self.product_info = pd.DataFrame(np.zeros((6, weeks)))
        self.product_info.index = {
            'Całkowite zapotrzebowanie',
            'Planowane przyjęcia',
            'Przewidywane na stanie',
            'Zapotrzebowanie netto',
            'Planowane zamówienia',
            'Planowane przyjęcie zamówień'
        }

    def info(self):
        print(self.product_info,'\n')






    