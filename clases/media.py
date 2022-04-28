from clases.grafico import *

class media(grafico):

    def __init__(self, dataset, columnauno, columnados):
        super().__init__(dataset, columnauno, columnados)

    def mediacalculada(self):
        self.dataset=pd.read_csv("pokemon.csv")
        def calcularfrecuencia():
            frecuencia= []
            for i in range (len(self.dataset)):
                resultado = self.dataset[self.columnauno][i]*self.dataset[self.columnados][i]
                frecuencia.append(resultado)
            return frecuencia
        self.dataset["frecuencia"]= calcularfrecuencia()
        sumafrecuencia = self.dataset["frecuencia"].sum()
        sumadeni = self.dataset[self.columnados].sum()
        return round(sumafrecuencia/sumadeni, 2)
