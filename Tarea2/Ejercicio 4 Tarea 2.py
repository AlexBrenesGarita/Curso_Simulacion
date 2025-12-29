#() Ejercicio 4
#Determine para cada generador congruencial mixto que se presenta a continuación si cumple con todo el período de m.

#a. x(0)   = 7
#   x(n+1) = ( 5 * x(n) + 24) mod 32
#b. x(0)   = 8
#   x(n+1) = ( 9 * x(n) + 13) mod 32
#c. x(0)   = 13
#   x(n+1) = (50 * x(n) + 17) mod 64
#d. x(0)   = 15
#   x(n+1) = ( 8 * x(n) + 16) mod 100
#e. x(0)   = 3
#   x(n+1) = ( 5 * x(n) + 21) mod 100

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


#a. x(0)   = 7
#   x(n+1) = ( 5 * x(n) + 24) mod 32

#congruencialMixto(7,5,24,32)
# Resultado = [7, 27, 31, 19, 23, 11, 15, 3, 7, 27, 31, 19, 23, 11, 15, 3, 7, 27, 31, 19, 23, 11, 15, 3, 7, 27, 31, 19, 23, 11, 15, 3, 7]
# Arreglo de elementos del recorrido sin repetir:  {3, 7, 11, 15, 19, 23, 27, 31}

# Al ejecutarlo podemos notar que el patron se repite varias veces y no cubre todo el periodo de m.

#b. x(0)   = 8
#   x(n+1) = ( 9 * x(n) + 13) mod 32

#congruencialMixto(8,9,13,32)
# Resultado = [8, 21, 10, 7, 12, 25, 14, 11, 16, 29, 18, 15, 20, 1, 22, 19, 24, 5, 26, 23, 28, 9, 30, 27, 0, 13, 2, 31, 4, 17, 6, 3, 8]
# Arreglo de elementos del recorrido sin repetir:  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}

# Al ejecutar podemos notar que este generador cumple con todo el periodo desde 0 a m - 1

#c. x(0)   = 13
#   x(n+1) = (50 * x(n) + 17) mod 64

#congruencialMixto(13,50,17,64)
# Resultado = [13, 27, 23, 15, 63, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 
# 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31]

# Arreglo de elementos del recorrido sin repetir:  {13, 15, 23, 27, 31, 63}

# Al ejecutar podemos notar que este generador no cumple con todo el periodo desde 0 a m - 1 ya que en cortas iteraciones el patron se bloquea en 31

#d. x(0)   = 15
#   x(n+1) = ( 8 * x(n) + 16) mod 100

#congruencialMixto(15,8,16,100)
# Resultado = [15, 36, 4, 48, 0, 16, 44, 68, 60, 96, 84, 88, 20, 76, 24, 8, 80, 56, 64, 28, 40, 36, 4, 48, 0, 16, 44, 68, 60, 96, 84, 88, 20, 76, 24, 8, 80, 56, 64, 28, 40, 36, 4, 
# 48, 0, 16, 44, 68, 60, 96, 84, 88, 20, 76, 24, 8, 80, 56, 64, 28, 40, 36, 4, 48, 0, 16, 44, 68, 60, 96, 84, 88, 20, 76, 24, 8, 80, 56, 64, 28, 40, 36, 4, 48, 0, 16, 44, 68, 60, 96, 84, 88, 20, 76, 24, 8, 80, 56, 64, 28, 40]

# Arreglo de elementos del recorrido sin repetir:  {0, 4, 8, 15, 16, 20, 24, 28, 36, 40, 44, 48, 56, 60, 64, 68, 76, 80, 84, 88, 96}

# Podemos observar que este no completa el periodo ya que a partir del 36 inicia el patron que se repite 5 veces

#e. x(0)   = 3
#   x(n+1) = ( 5 * x(n) + 21) mod 100

#congruencialMixto(3,5,21,100)
# Resultado = [3, 36, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 
# 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51, 76, 1, 26, 51]

# Arreglo de elementos del recorrido sin repetir:  {1, 3, 36, 76, 51, 26}
# Con los resultados podemos observar que a partir del 1 se genera un patron que no permite que se complete todo el periodo