#() Ejercicio 2
#Para 5 bits construya un método congruencial binario que realice un recorrido completo. Indique cuál es la semilla y cuál es la operación que realiza. 

#Primero es necesario mencionar que se va a utilizar las herramientas binarias de python como el prefijo 0b para representar binarios y los operadores >> , ^ y | para el shift a la derecha, para el xor y para el or respectivamente.
#Utilizando el metodo congruencial binario solo se puede alcanzar 31 elementos dentro de los 5 bits ya que el 0 no permite el correcto funcionamiento por lo que se colocara una validacion para evitar su uso,ademas 
#utilizando los dos bits menos significativos topamos con el problema de que el maximo recorrido se repite cada 21 elementos por lo que haciendo un ajuste usamos el primer y tercer bit menos significativo
#ya que de esta forma el polinomio generado garantiza un recorrido completo.

#Para esta prueba se usa la semilla 01010 que corresponde a 10 decimal y se toma el primer y tercer bit menos significativos usando desplazamientos, luego se realizar un xor entre ambos bits para al final mezclar por medio de un or
#el numero binario actual con el bit mas significativo reemplazado por el bit sacado de la operacion del cor
def congruencialBinario5bits(semilla=0b01010):
    if semilla == 0:
        return "La semilla del congruencial binario no puede ser 0"

    recorrido = 32
    elementos = []
    actual = semilla & 0b11111

    for i in range(recorrido):
        elementos.append(actual)

        bit0 = actual & 0b1
        bit2 = (actual >> 2) & 0b1

        nuevoBit = bit0 ^ bit2
        actual = (actual >> 1) | (nuevoBit << 4) # Se realiza un or del actual con dividido entre 2 y el bit sacado del xor multiplicado por 2^4

    return elementos


resultado= congruencialBinario5bits()
print(resultado)
if not isinstance(resultado,str):
    print(len(resultado))