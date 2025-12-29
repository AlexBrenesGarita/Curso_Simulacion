#() Ejercicio 7
#Defina los parametros de a, c, x(0) para un recorrido completo con el valor
#de m = 9.

def lcg_mixed_step(a, c, m):
    return lambda x: (a * x + c) % m


def generate(a, c, m, x0, n):
    f = lcg_mixed_step(a, c, m)
    x = x0
    out = [x]
    for _ in range(n - 1):
        x = f(x)
        out.append(x)
    return out


def main():
    print("=== Ejercicio 7: Mixto con m=9 (recorrido completo) ===\n")

    a, c, m, x0 = 4, 1, 9, 0
    seq = generate(a, c, m, x0, n=m)

    print("Parámetros: a={}, c={}, m={}, x0={}".format(a, c, m, x0))
    print("Secuencia (9 valores):")
    print(seq)

    seen = set(seq)
    ok = (len(seen) == m)
    print("\nValores distintos generados:", sorted(seen))
    print("¿Recorre 0..8 completo? {}".format("SI" if ok else "NO"))


if __name__ == "__main__":
    main()
