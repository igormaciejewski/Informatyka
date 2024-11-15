def Zad1():
    def scalanie(tab, lewy, srodek, prawy):
        pom = []
        i, j = lewy, srodek + 1
        while i <= srodek and j <= prawy:
            if tab[i] < tab[j]:
                pom.append(tab[i])
                i += 1
            else:
                pom.append(tab[j])
                j += 1
        while i <= srodek:
            pom.append(tab[i])
            i += 1
        while j <= prawy:
            pom.append(tab[j])
            j += 1
        for k in range(len(pom)):
            tab[lewy + k] = pom[k]

    def sortuj(tab, lewy, prawy):
        if lewy < prawy:
            srodek = (prawy + lewy) // 2
            sortuj(tab, lewy, srodek)
            sortuj(tab, srodek + 1, prawy)
            scalanie(tab, lewy, srodek, prawy)
    
    ciag = input("Wprowadź ciąg liczb rozdzielonych spacjami: ")
    arr = list(map(int, ciag.split()))
    sortuj(arr, 0, len(arr) - 1)
    print("Posortowany ciąg:", arr)

def Zad2():
    def wczytaj_ciagi_z_pliku(nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            ciagi = plik.readlines()
        ciag1 = list(map(int, ciagi[0].strip().split()))
        ciag2 = list(map(int, ciagi[1].strip().split()))
        return ciag1, ciag2

    def zapisz_do_pliku(nazwa_pliku, ciag):
        with open(nazwa_pliku, 'w') as plik:
            plik.write(' '.join(map(str, ciag)))

    def scal_i_zapisz(ciag1, ciag2, nazwa_wyjscia):
        scalony_ciag = sorted(ciag1 + ciag2)
        zapisz_do_pliku(nazwa_wyjscia, scalony_ciag)
        print("Scalony i posortowany ciag:", scalony_ciag)

    ciag1, ciag2 = wczytaj_ciagi_z_pliku('C:\\Users\\spide\\Desktop\\Technikum\\INformatyka\\klasa 3\\07\\ciagi.txt')
    scal_i_zapisz(ciag1, ciag2, 'C:\\Users\\spide\\Desktop\\Technikum\\INformatyka\\klasa 3\\07\\wyniki_2.txt')
Zad1()
Zad2()