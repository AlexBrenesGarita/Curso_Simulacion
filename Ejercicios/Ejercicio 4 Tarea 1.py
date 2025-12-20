#Ejercicio 4 
'''
Se tiene un mazo de cartas convencional.
a. Cuál es la probabilidad de sacar dos cartas y que ambos sean ases?
b. Construya un programa de simulación que genere estos resultados.
Sugerencia: La probabilidad es: 1/221 ~ 0.0045
'''


import random

def prob_dos_ases(trials=300_000):
    ##Simula el sorteo de 2 cartas sin reemplazo de una baraja con 4 ases y 48 no-ases.
    deck = ["A"] * 4 + ["X"] * 48 #A = as, X = no-as
    hits = 0

    for _ in range(trials):
        #Se sacan 2 cartas sin reemplazo
        hand = random.sample(deck, 2) 
        #Se verifica si ambas son ases
        if hand.count("A") == 2:
            hits += 1

    return hits / trials

print(prob_dos_ases())
