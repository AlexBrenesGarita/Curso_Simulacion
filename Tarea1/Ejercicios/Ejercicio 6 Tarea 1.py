#Ejercicio 6
'''
Se tiene un mazo de cartas convencional, el cual ha sido barajdo. Se reparten 5 cartas y se desea establecer la probabilidad que dentro de esas 5 cartas se encuentre un par de ases.
a. Resuelva el problema utilizando probabilidad clásica.
b. Resuelva el problema construyendo un programa de simulación.

'''

import random
from math import comb

#Funcion para calcular la probabilidad clasica de obtener un par de ases al sacar 5 cartas
def prob_par_de_ases_clasica():
    return comb(4, 2) * comb(48, 3) / comb(52, 5)


#Funcion para calcular la probabilidad por simulacion de obtener un par de ases al sacar 5 cartas
def prob_par_de_ases_sim(trials=300_000):
    deck = ["A"] * 4 + ["X"] * 48
    hits = 0

    for _ in range(trials):
        hand = random.sample(deck, 5)
        if hand.count("A") == 2:
            hits += 1

    return hits / trials

#Imprime la probabilidad clasica y simulada de obtener un par de ases
print("Clasica:", prob_par_de_ases_clasica())
print("Simulada:", prob_par_de_ases_sim())
