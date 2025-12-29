#() Ejercicio 3.
#Utilizando el lenguaje de simulación, construya una distribución binomial con un máximo de 3 éxitos y 
#una probabilidad de obtener un éxito de 0.50. Grafique un histograma con los resultados obtenidos.
#Sugerencia: Busque las instrucciones BINOMIALPROB e HISTOGRAM.

#Vamos a usar matplotlib para la construccion del histograma y random para el manejo de aciertos y fallos
import matplotlib.pyplot as plt
import random as r

# Función binomial
def binomial(n, p, simulaciones):
    resultados = []

    for i in range(simulaciones):
        aciertos = 0
        for j in range(n):
            if r.random() <= p:
                aciertos += 1
        resultados.append(aciertos)

    return resultados

# Parámetros
n = 3
p = 0.50
simulaciones = 15000

# Simulación
datos = binomial(n, p, simulaciones)

# Histograma
plt.hist(datos, bins=range(0, n+2), align='left', rwidth=0.8)
plt.xlabel("Número de éxitos")
plt.ylabel("Frecuencia")
plt.title("Distribución Binomial (n=3, p=0.50)")
plt.xticks(range(0, n+1))
plt.show()

