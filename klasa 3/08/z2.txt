def oblicz_wartosc_wielomianu_horner(wspolczynniki, x):
    n = len(wspolczynniki) - 1
    y = wspolczynniki[n]
    for i in range(n - 1, -1, -1):
        y = y * x + wspolczynniki[i]
    return y

wspolczynniki_str = input("Podaj współczynniki wielomianu, oddzielając je spacjami (np. '2 -3 0 5'): ")
wspolczynniki = list(map(float, wspolczynniki_str.split()))

x = float(input("Podaj wartość x: "))

wynik = oblicz_wartosc_wielomianu_horner(wspolczynniki, x)

print(f"Wartość wielomianu dla x = {x} wynosi: {wynik}")
