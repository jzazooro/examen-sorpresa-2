from turtle import title
import pandas as pd
import matplotlib.pyplot as plt

class grafico:

    def __init__(self, dataset, columnauno, columnados):
        self.dataset=dataset
        self.columnauno=columnauno
        self.columnados=columnados
    
    def grafica(self, title):
        self.dataset=pd.read_csv("pokemon.csv")
        self.dataset.groupby(self.columnauno)[self.columnados].sum().plot(kind='bar')
        plt.title(title)
        plt.xlabel(None)
        plt.show()
        

