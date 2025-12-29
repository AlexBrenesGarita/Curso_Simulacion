#() Ejercicio 10
#Se tiene un generador aleatorio de un sólo dígito. Es decir puede generar de manera uniforme los valores 0,1,2,3,4,5,6,7,8 y 9. Para cada uno de los siguientes fenómenos indique como utilizaría este generador.

#a. Para generar una moneda legal, con 0.50 de probabilidad de que salga corona y 0.50 de probabilidad que salga escudo.
#b. Para generar el siguiente fenómeno, probabilidad de a es 0.10, la probabilidad de b es 0.40 y la probabilidad de c es 0.50.
#c. Para generar los valores de arrojar un dado.
#d. Si en lugar de un generador aleatorio entre [0,9] se tiene un generador de números aleatorios entre [0,99] indique cómo realizaría la asignación de probabilidades anterior.

#Para este ejercicio vamos a usar randrange para simular los numeros aleatorios y vamos a suponer que los unicos numeros  que se pueden generar son enteros y de un digito (0,1,2,3,4,5,6,7,8,9)

from random import randrange

#a. Para generar una moneda legal, con 0.50 de probabilidad de que salga corona y 0.50 de probabilidad que salga escudo.

# En este problema simplemente se parte a la mitad los numeros generables, del 0 al 4 corresponden a escudos y el resto de 5 a 9 corresponde a coronas.
def moneda(simulaciones):
    escudos=0
    coronas=0
    intento=0
    for i in range(simulaciones):
        intento = randrange(0,10,1)
        if intento < 5:
            escudos+=1
            continue
        coronas+=1
    print("Escudos: ",escudos/simulaciones)
    print("Coronas: ",coronas/simulaciones)

#moneda(1000000)

#b. Para generar el siguiente fenómeno, probabilidad de a es 0.10, la probabilidad de b es 0.40 y la probabilidad de c es 0.50.

# Este problema se resuelve de una manera similar al anterior solamente se divide las areas de manera distinta.
def problemaB(simulaciones):
    a=0
    b=0
    c=0
    intento=0
    for i in range(simulaciones):
        intento = randrange(0,10,1)
        if intento == 1:
            a+=1
            continue
        if intento > 1 and intento <= 5:
            b+=1
            continue
        c+=1
    print("Probabilidad a: ",a/simulaciones)
    print("Probabilidad b: ",b/simulaciones)
    print("Probabilidad c: ",c/simulaciones)

# problemaB(1000000)

#c. Para generar los valores de arrojar un dado.

# Para este problema suponiendo que solo se generan numeros enteros de un solo digito agrupan los valores en los que se van a usar para el calculo y los que se van a desechar y rehacer
# para eso se usan los numeros del 1 al 6 para el calculo y en caso de que algun numero no pertenezca a ese grupo se rehace el intento
def dado(simulaciones):
    uno=0
    dos=0
    tres=0
    cuatro=0
    cinco=0
    seis=0
    i=0
    while i != simulaciones:
        intento = randrange(0,10,1)
        if intento == 1:
            uno+=1
            i+=1
            continue
        elif intento == 2:
            dos+=1
            i+=1
            continue
        elif intento == 3:
            tres+=1
            i+=1
            continue
        elif intento == 4:
            cuatro+=1
            i+=1
            continue
        elif intento == 5:
            cinco+=1
            i+=1
            continue
        elif intento == 6:
            seis+=1
            i+=1
            continue
        else:
            continue

    print("Probabilidad 1: ",uno/simulaciones)
    print("Probabilidad 2: ",dos/simulaciones)
    print("Probabilidad 3: ",tres/simulaciones)
    print("Probabilidad 4: ",cuatro/simulaciones)
    print("Probabilidad 5: ",cinco/simulaciones)
    print("Probabilidad 6: ",seis/simulaciones)

#dado(1000000)

#d. Si en lugar de un generador aleatorio entre [0,9] se tiene un generador de numeros aleatorios entre [0,99] indique como realizaria la asignacion de probabilidades anterior y considere ¿Se pueden simular dados con todos los poliedros regulares?.

#Este ejercicio se resuelve como la version normal solo que se adapta los grupos para abarcar una mayor cantidad
def ejercicioAAumentado(simulaciones):
    aciertos=0
    fallos=0
    intento=0
    for i in range(simulaciones):
        intento = randrange(0,100,1)
        if intento < 50:
            aciertos+=1
            continue
        fallos+=1
    print("Escudos: ",aciertos/simulaciones)
    print("Coronas: ",fallos/simulaciones)

#ejercicioAAumentado(1000000)

#Este ejercicio se resuelve como la version normal solo que se adapta los grupos para abarcar una mayor cantidad
def ejercicioBAumentado(simulaciones):
    a=0
    b=0
    c=0
    intento=0
    for i in range(simulaciones):
        intento = randrange(0,100,1)
        if intento < 10:
            a+=1
            continue
        if intento > 10 and intento <= 50:
            b+=1
            continue
        c+=1
    print("Probabilidad a: ",a/simulaciones)
    print("Probabilidad b: ",b/simulaciones)
    print("Probabilidad c: ",c/simulaciones)

#ejercicioBAumentado(1000000)

#Para la version adaptada del ejercicio c se puede decir que se pueden simular todos los poliedros regulares utilizando la mayor cantidad posible de numeros dentro del rango, pero no todos usan el rango completo

# Para el tetraedro se guarda en un arreglo con cuatro espacios que representan cada cara, luego se define la cara que se va a incrementar de acuerdo al divisor que represente al grupo de la cara, en este caso
# 25 ya que 100/4 es 25 por lo que cada cara va a tener 25 elementos
# 1/4 = 0.24
def tetraedro(simulaciones):
    caras = [0,0,0,0]
    i=0
    while i != simulaciones:
        intento = randrange(0,100,1)
        cara = intento // 25
        caras[cara] += 1
        i += 1

    for j in range(4):
        print(f"Probabilidad {j+1}: {caras[j]/simulaciones}")

#tetraedro(1000000)

# Para el cubo se guarda en un arreglo con seis espacios que representan cada cara, tambien, es necesario conseguir el maximo numero menor a 100 que sea divisible por 6, en este caso 96, luego se define la cara usando el divisor de grupo, en este caso
# 16 ya que 96/6 es 16 por lo que cada cara va a tener 16 elementos y si es mayor a 96 se rehace el intento
# 1/6 = 0.1666666667
def cubo(simulaciones):
    caras = [0,0,0,0,0,0]
    i = 0

    while i != simulaciones:
        intento = randrange(0,100,1)
        if intento < 96:
            cara = intento // 16
            caras[cara] += 1
            i += 1

    for j in range(6):
        print(f"Probabilidad {j+1}: {caras[j]/simulaciones}")


#cubo(1000000)

# Para el octaedro se guarda en un arreglo con ocho espacios que representan cada cara, tambien, es necesario conseguir el maximo numero menor a 100 que sea divisible por 8, en este caso 88, luego se define la cara usando el divisor de grupo, en este caso
# 11 ya que 88/8 es 11 por lo que cada cara va a tener 11 elementos y si es mayor a 88 se rehace el intento
# 1/8 = 0.125
def octaedro(simulaciones):
    caras = [0,0,0,0,0,0,0,0]
    i = 0

    while i != simulaciones:
        intento = randrange(0,100,1)
        if intento < 88:
            cara = intento // 11
            caras[cara] += 1
            i += 1

    for j in range(8):
        print(f"Probabilidad {j+1}: {caras[j]/simulaciones}")
#octaedro(1000000)

# Para el dodecaedro se guarda en un arreglo con doce espacios que representan cada cara, tambien es necesario conseguir el maximo numero menor a 100 que sea divisible por 12, en este caso 96, luego se define la cara usando el divisor de grupo, en este caso
# 8 ya que 96/12 es 8 por lo que cada cara va a tener 8 elementos y si es mayor a 96 se rehace el intento
# 1/12 = 0.0833333333
def dodecaedro(simulaciones):
    caras = [0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0

    while i != simulaciones:
        intento = randrange(0,100,1)
        if intento < 96:
            cara = intento // 8
            caras[cara] += 1
            i += 1

    for j in range(12):
        print(f"Probabilidad {j+1}: {caras[j]/simulaciones}")

#dodecaedro(1000000)

# Para el icosaedro se guarda en un arreglo con veinte espacios que representan cada cara, luego se define la cara usando el divisor de grupo, en este caso
# 5 ya que 100/20 es 5 por lo que cada cara va a tener 5 elementos.
# 1/20 = 0.05
def icosaedro(simulaciones):
    caras = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0

    while i != simulaciones:
        intento = randrange(0,100,1)
        cara = intento // 5
        caras[cara] += 1
        i += 1

    for j in range(20):
        print(f"Probabilidad {j+1}: {caras[j]/simulaciones}")

#icosaedro(1000000)