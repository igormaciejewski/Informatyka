def scal(t1, t2):
    wynik = []
    n1 = len(t1)
    n2 = len(t2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            wynik.append(t1[i])
            i += 1
        else:
            wynik.append(t2[j])
            j += 1
    wynik.extend(t1[i:])
    wynik.extend(t2[j:])
    return wynik

def sortowanie_przez_scalanie(t):
    n = len(t)
    if n > 1:
        srodek = (n - 1) // 2
        lewy = sortowanie_przez_scalanie(t[:srodek + 1])
        prawy = sortowanie_przez_scalanie(t[srodek + 1:])
        return scal(lewy, prawy)
    return t

ciag = input("Podaj ciag: ")
t = list(map(int, ciag.split()))
sorted_t = sortowanie_przez_scalanie(t)
print("Posortowany ciag:", sorted_t)
