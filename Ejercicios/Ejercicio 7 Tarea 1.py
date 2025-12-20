#() Ejercicio 7. 
#Se tiene un mazo de cartas convencional, el cual ha sido barajdo. Se reparten 5 cartas y se desea establecer la probabilidad que las 5 cartas sumen entre 17 y 21.
#Resuelva el problema construyendo un programa de simulación.

import random as r

#Para este ejercicio vamos a usar los mismos objetos del ejercicio 5

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
        
def sumarValores(arreglo):
    if arreglo == []:
        return 0
    return arreglo[0] + sumarValores(arreglo[1:])

def SimulacionDeMano(cantidad):
    aciertos=0
    for i in range(cantidad):
        valor=0
        baraja = Baraja()
        cartas= []
        #Tomar 5 cartas
        cartas.append(baraja.tomarCarta().getValor())
        cartas.append(baraja.tomarCarta().getValor())
        cartas.append(baraja.tomarCarta().getValor())
        cartas.append(baraja.tomarCarta().getValor())
        cartas.append(baraja.tomarCarta().getValor())

        valor = sumarValores(cartas)
        while valor < 21:
            if not 14 in cartas:
                break
            cartas.remove(14)
            cartas.append(1)
            valor = sumarValores(cartas)
            
        if valor >= 17 and valor <= 21:
            aciertos+=1

    return aciertos/cantidad

resultado = SimulacionDeMano(100000)
print(f'Probabilidad Calculada: {resultado}')