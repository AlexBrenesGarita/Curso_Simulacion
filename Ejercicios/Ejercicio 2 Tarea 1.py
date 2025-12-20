#Ejercicio 2
'''
Se tienen 3 monedas. Las cuales pueden dar como resultado escudo o corona.
a. Utilizando probabilidad matemática calcule el valor de obtener dos coronas.
b. Con un programa de simulación, calcule la probabilidad de obtener 0 coronas.
c. Con un programa de simulación, calcule la probabilidad de obtener 1 coronas.
d. Con un programa de simulación, calcule la probabilidad de obtener 2 coronas.
e. Con un programa de simulación, calcule la probabilidad de obtener 3 coronas.
f. Qué clase de distribución de probabilidad es esta?

Sugerencia:
Probabilidad de obtener 0 coronas: 0.125
Probabilidad de obtener 1 corona:  0.375
Probabilidad de obtener 2 coronas: 0.375
Probabilidad de obtener 3 coronas: 0.125
'''

import random

#Funcion para simular el lanzamiento de 3 monedas y contar coronas
def sim_3_monedas(trials=200_000):
    #Contamos de 0 a 3 coronas posibles
    counts = [0, 0, 0, 0]

    for _ in range(trials):
        coronas = 0
        for _ in range(3):
            #Simulamos el lanzamiento de una moneda
            if random.random() <= 0.5:
                coronas += 1
        counts[coronas] += 1

    probs = [c / trials for c in counts]
    return probs  #[P(0), P(1), P(2), P(3)]

p0, p1, p2, p3 = sim_3_monedas()
print("P(0) =", p0)
print("P(1) =", p1)
print("P(2) =", p2)
print("P(3) =", p3)
