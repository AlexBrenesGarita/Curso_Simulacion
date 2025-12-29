#Ejercicio 8
'''
Se tiene un juego con una probabilidad de ganar de 0.48 y una probabilidad de perder de 0.52. Cada vez que se apuesta una cantidad de dinero se gana lo que se apuesta o se pierde todo. Se inicia el juego con $100 dólares y se desea llegar a obtener $200.
a. Si se utiliza una estrategia de apuesta (x,x) con x=10. Es decir, si gano apuesto "x" y si pierdo apuesto "x", determine la probabilidad de obtener la cantidad deseada.
b. Si se utiliza una estrategia de apuesta (x,2*x) con x=10. Es decir, si gano apuesto "x", pero si pierdo apuesto el doble de lo que perdí 2*x, determine la probabilidad de obtener la cantidad deseada.
'''

import random

#Probabilidad de ganar cada apuesta
P_WIN = 0.48

#Funcion para simular la estrategia de apuesta hasta llegar a 200 o quedarse sin dinero
def sim_objetivo_200(trials=100_000, x=10):
    hits = 0
    for _ in range(trials):
        #Empieza con 100 de dinero
        money = 100
        while 0 < money < 200:
            #Apuesta lo minimo entre x y el dinero que tiene
            bet = min(x, money) 
            if random.random() < P_WIN:
                money += bet
            else:
                money -= bet
        if money >= 200:
            hits += 1
    return hits / trials

#Imprime la probabilidad simulada de alcanzar los 200 dolares con la estrategia (x,x)
print(sim_objetivo_200())
