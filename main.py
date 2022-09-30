def bubble_sort(szamok):
    n = len(szamok)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if szamok[j] > szamok[j + 1]:
                szamok[j], szamok[j + 1] = szamok[j + 1], szamok[j]
                already_sorted = False
        if already_sorted:
            break

    return szamok

szamok = []
uj_lista = []
db = 0

while db <= 6:
    szam = int(input("Kérem a számot!: "))
    szamok.append(szam)
    db += 1

uj_lista = bubble_sort(szamok)
print(szamok)
print(uj_lista)
