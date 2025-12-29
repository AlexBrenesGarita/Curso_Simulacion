#() Ejercicio 3
#Genere 50 numeros aleatorios de 4 dıgitos utilizando el generador de cuadrados
#medios utilizando los siguientes par´ametros.

#a. x0 = 3567345
#b. x0 = 1234500012
#c. x0 = 4567234902

def middle_square_next(seed, k=4):
    sq = seed * seed
    s = str(sq)
    if len(s) < k:
        s = s.zfill(k)
    start = (len(s) - k) // 2
    return int(s[start:start + k])


def middle_square_sequence(seed, k=4, n=50):
    x = seed
    out = []
    for _ in range(n):
        x = middle_square_next(x, k)
        out.append(x)
    return out


def print_50(seed):
    xs = middle_square_sequence(seed, k=4, n=50)
    print("\nSemilla x(0)={}".format(seed))
    for i in range(0, 50, 10):
        chunk = xs[i:i + 10]
        line = " ".join("{:04d}".format(v) for v in chunk)
        print("x({:02d})..x({:02d}): {}".format(i + 1, i + len(chunk), line))


def main():
    print("=== Ejercicio 3: Cuadrados medios (k=4, 50 numeros) ===")
    for s in [3567345, 1234500012, 4567234902]:
        print_50(s)


if __name__ == "__main__":
    main()