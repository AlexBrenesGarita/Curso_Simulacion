#() Ejercicio 9
#Utilizando las variantes del meetodo congruencial mixto, el metodo congruencial
#multiplicativo y el metodo congruencial aditivo encuentre generadores
#para numeros de 0 hasta 9 que tengan un recorrido completo.

def lcg_mixed_step(a, c, m):
    return lambda x: (a * x + c) % m


def lcg_mult_step(a, m):
    return lambda x: (a * x) % m


def additive_sequence(x0, x1, m, n):
    out = [x0, x1]
    a, b = x0, x1
    for _ in range(n - 2):
        a, b = b, (a + b) % m
        out.append(b)
    return out


def main():
    print("=== Ejercicio 9: Generadores para 0..9 ===\n")

    # a) mixto (sumar 1 mod 10)
    print("a) Mixto con período 10: x(n+1) = (x(n) + 1) mod 10")
    f = lcg_mixed_step(a=1, c=1, m=10)
    x = 0
    seq_a = []
    for _ in range(10):
        seq_a.append(x)
        x = f(x)
    print("   Primeros 10:", seq_a)
    print("   Distintos:", sorted(set(seq_a)))
    print("")

    # b) multiplicativo mod 11 y mapeo a 0..9
    print("b) Multiplicativo mod 11: x(n+1)=(2x) mod 11, x0=1; luego y=x-1")
    g = lcg_mult_step(a=2, m=11)
    x = 1
    xs = []
    for _ in range(10):
        xs.append(x)
        x = g(x)
    ys = [v - 1 for v in xs]
    print("   x (10 valores):", xs)
    print("   y=x-1:", ys)
    print("   y distintos:", sorted(set(ys)))
    print("")

    # c) aditivo Fibonacci mod 10
    print("c) Aditivo (Fibonacci) mod 10: x(n+1)=(x(n)+x(n-1)) mod 10, x0=0, x1=1")
    seq_c = additive_sequence(0, 1, 10, n=20)
    print("   Primeros 20:", seq_c)
    print("   Digitos vistos:", sorted(set(seq_c)))


if __name__ == "__main__":
    main()
