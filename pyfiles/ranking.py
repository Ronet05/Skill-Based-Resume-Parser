import numpy as np
import pandas as pd
import csv
class Ranker:
    def rank_csv(self):
        df=pd.read_csv("cv_list.csv")
        sortedlist=df.sort_values(['Score'],ascending=False)
        l=sortedlist.values
        return l

        