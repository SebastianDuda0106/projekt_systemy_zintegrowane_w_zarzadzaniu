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


    def createTable(self, weeks):
        list = []
        for i in range(weeks):
            list.append(0)
        self.product_info = pd.DataFrame(np.zeros((3, weeks)))
        self.product_info.index = {
            'Przewidywany popyt',
            'Produkcja',
            'Dostępne'
            }
        
    def info(self):
        print(self.product_info,'\n')