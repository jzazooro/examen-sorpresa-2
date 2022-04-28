from clases.media import*
from clases.grafico import*

class desviaciontipica(media):
    def __init__(self, dataset, columnauno, columnados):
        super().__init__(dataset, columnauno, columnados)
    def calculodesviaciontipica(self):
        self.dataset=pd.read_csv("pokemon.csv")
        def columnadesviaciontipica():
            columna=[]
            media=self.mediacalculada()
            for i in range (len(self.dataset)):
                solucion=self.dataset[self.columnados][i]*(self.dataset[self.columnauno][i]-media)*(self.dataset[self.columnauno][i]-media)
                columna.append(solucion)
            return columna
        self.dataset["Ni*((xi-media)^2"]=columna_desviaciontipica()
        sumacolumnas=self.dataset["Ni*((xi-media)^2"].sum()
        suma_frecuencia=self.dataset["Xini"].sum()
        varianza=sum_columna/sumadeni
            
