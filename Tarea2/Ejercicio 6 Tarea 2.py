#() Ejercicio 6
#Utilice el método congruencial mixto y encuentre los parámetros adecuados de x(0), b, c y m para generar un recorrido completo de números entre 0 y 14.

# Es necesario mencionar que se va a usar la funcion del ejercicio 4 congruencial mixto para calcular el recorrido completo
# Vamos a comenzar eligiendo el modulo que seria el modulo 15, necesario para que el recorrido completo este entre 0 y 14 ya que m representa la secuencia de numeros desde 0 a m-1
# Vamos a usar 16 como multiplicador ya que al despejar la congruencia de a con 0 de acuerdo al modulo del minimo comun multiplo de los factores de m se obtiene 16.
# Para la constante vamos a usar c = 1 ya que se recomienda en general.
# Para la seleccion de la semilla la unica restriccion es que sea menor al modulo por lo que escogeremos x0=1 por lo que tendriamos lo siguiente:

# x(0) = 1
# x(n+1) = ( 13 * x(n) + 1) mod 15
def congruencialMixto(semilla,multiplicador,constante,modulo):
    recorrido = []
    anterior= semilla
    i=1
    while i <= modulo+1: #Se agrega uno para ver si el patron se repite en caso de que alguno tenga todo el periodo de m
        recorrido.append(anterior)
        anterior= (multiplicador * anterior + constante)% modulo
        i+=1
    print(recorrido)
    print("Arreglo de elementos del recorrido sin repetir: ",set(recorrido))


congruencialMixto(12,16,1,15)