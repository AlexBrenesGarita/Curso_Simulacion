#() Ejercicio 1
#Utilice el metodo congruencial binario pero en lugar de realizar un xor
#con las posiciones 0 y 1, de derecha a izquierda, realice un xor con las
#posiciones 0 y 2. Utilice las siguientes semillas y muestre si realiza todo el
#recorrido o no.

#a. x0 = 110
#b. x0 = 1111

#Retorna (mu, lam) donde lam es el periodo (longitud del ciclo)
def floyd_cycle(f, x0):
    tortoise = f(x0)
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return mu, lam

#Un paso del generador binario xor+shift
def lfsr_step(state, n_bits, taps=(0, 2)):   
    xor_bit = 0
    for t in taps:
        xor_bit ^= (state >> t) & 1

    mask = (1 << n_bits) - 1
    return ((xor_bit << (n_bits - 1)) | (state >> 1)) & mask


def period_from_seed(seed, n_bits, taps=(0, 2)):
    f = lambda x: lfsr_step(x, n_bits, taps)
    mu, lam = floyd_cycle(f, seed)
    return lam


def fmt_bin(x, n_bits):
    return format(x, "0{}b".format(n_bits))


def print_sequence(seed, n_bits, steps=12):
    x = seed
    print("Semilla x(0) = {} ({})".format(fmt_bin(seed, n_bits), seed))
    print("Estados:")
    for i in range(steps):
        print("  x({}) = {} -> {}".format(i, fmt_bin(x, n_bits), x))
        x = lfsr_step(x, n_bits)
    print("Periodo (desde la semilla): {}".format(period_from_seed(seed, n_bits)))


def main():
    print("=== Ejercicio 1: Generador binario (xor taps 0 y 2, shift derecha) ===\n")

    print("a) x(0)=110 (3 bits)")
    print_sequence(seed=0b110, n_bits=3, steps=10)

    print("\n" + "-" * 60 + "\n")

    print("b) x(0)=1111 (4 bits)")
    print_sequence(seed=0b1111, n_bits=4, steps=10)


if __name__ == "__main__":
    main()
