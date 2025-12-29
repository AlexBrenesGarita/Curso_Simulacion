#() Ejercicio 5
#Determine para cada generador congruencial multiplicativo que se presenta
#a continuacion si cumple con todo el perıodo de m. La expresion ab
#significa a elevado a la potencia b.

#a. x0 = 7
#xn+1 = (5 × xn)(26)
#b. x0 = 9
#xn+1 = (11 × xn)(27)
#c. x0 = 3
#xn+1 = (221 × xn)(103)
#d. x0 = 17
#xn+1 = (203 × xn)(105)
#e. x0 = 19
#xn+1 = (211 × xn)(108)

def floyd_cycle(f, x0):
    """Retorna (mu, lam) donde lam es el periodo (longitud del ciclo)."""
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


def lcg_mult_step(a, m):
    return lambda x: (a * x) % m


def main():
    print("=== Ejercicio 5: Congruencial multiplicativo (período con semilla dada) ===\n")

    cases = [
        ("a", 5, 2**6, 7),
        ("b", 11, 2**7, 9),
        ("c", 221, 10**3, 3),
        ("d", 203, 10**5, 17),
        ("e", 211, 10**8, 19),
    ]

    for label, a, m, x0 in cases:
        f = lcg_mult_step(a, m)
        mu, lam = floyd_cycle(f, x0)
        print("{} ) a={}, m={}, x0={}".format(label, a, m, x0))
        print("    mu={}, período={}".format(mu, lam))
        print("    ¿Periodo completo (=m)? {}".format("SI" if lam == m else "NO"))
        print("")


if __name__ == "__main__":
    main()