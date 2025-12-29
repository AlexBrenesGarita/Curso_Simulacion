#() Ejercicio 5.

#Se tiene un mazo de cartas convencional.
#a. Cuál es la probabilidad que al sacar una carta se obtenga una espada o un trébol?
#b. Construya un programa de simulación que genere estos resultados.
#Sugerencia: La probabilidad es: 0.50

#Para este caso vamos a simular una baraja de cartas convencional por medio de objetos
import random as r

class Baraja:
    def __init__(self):
        self.Cartas = []
        self.tipos = ['Corazones','Espadas','Treboles','Diamantes']
        self.armarBaraja()
        self.barajar()
    
    def armarBaraja(self):
        for tipo in self.tipos:
            for valor in range(2,15):
                self.Cartas.append(Carta(valor,tipo))
    
    def barajar(self):
        r.shuffle(self.Cartas)

    def tomarCarta(self):
        return self.Cartas.pop(0)

class Carta:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
    def getValor(self):
        return self.valor
    def getTipo(self):
        return self.tipo
        

def probColorNegro(cantidad):
    aciertos=0
    totales=0
    for i in range(cantidad):
        baraja = Baraja()
        carta = baraja.tomarCarta()
        if carta.getTipo() in ['Espadas','Treboles']:
            aciertos+=1
            totales+=1
            continue
        totales+=1
    return aciertos / totales


resultado = probColorNegro(10000)
print(f'Probabilidad Calculada: {resultado}')
            

        