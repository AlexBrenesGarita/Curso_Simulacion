#() Ejercicio 8
#Defina los parámetros de a, c, x(0) para un recorrido completo con el valor de m = 19.

# Se va a usar la funcion congruencialMixto del ejercicio 4
# Ya que tenemos a m = 19 vamos a decir que c = 1 ya que recomiendan el numero, la unica restriccion de la semilla es que sea menor a 19 por lo que usamos x0= 5
# elegimos a = 20 ya que al despejar la congruencia de a con 0 de acuerdo al modulo del minimo comun multiplo de los factores de m se obtiene 20.
# Con todos los datos tenemos lo siguiente:
# x(0) = 5
# x(n+1) = ( 20 * x(n) + 1) mod 19

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

congruencialMixto(5,20,1,19)