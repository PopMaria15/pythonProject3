# 1.sa se determine valoarea minima si maxima dintr-o matrice de dimensiune nxm

"""2.sa se genereze valorile unei matrice patratice dupa urmatoarele reguli:
- elem pentru care produsul indicilor este un numar par vor avea valoarea 1
- elem pentru care produsul indicilor este un numar impar vor avea valoarea 0
- elem de pe diagonala principala vor avea valoarea 2"""

def min_max_matrice():
    n = int(input("Introduceti nr de linii: "))
    m = int(input("Introduceti nr de coloane: "))
    matrix = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
             print(i, ",", j, ":", end=" ")
             matrix[i][j] = int(input())
    minim = matrix[0][0]
    maxim = matrix[0][0]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < minim:
                minim = matrix[i][j]
            if matrix[i][j] > maxim:
                maxim = matrix[i][j]
    print("Valoarea minima este: ", minim)
    print("Valoarea maxima este: ", maxim)


def matrice_generata():
    n = int(input("Introduceti marimea matricei: "))
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i*j % 2 == 0:
                matrix[i][j] = 1
            if i*j % 2 != 0:
                matrix[i][j] = 0
            if i == j:
                matrix[i][j] = 2
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
    print("")


def unire(listas, listad):
    rezultat = []
    i = j = 0
    while i < len(listas) and j < len(listad):
        if listas[i] < listad[j]:
            rezultat.append(listas[i])
            i += 1
        else:
            rezultat.append(listad[j])
            j += 1
    while i < len(listas):
        rezultat.append(listas[i])
        i += 1
    while j < len(listad):
        rezultat.append(listad[j])
        j += 1
    return rezultat


def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mijloc = len(lista) // 2
        stanga = merge_sort(lista[:mijloc])
        dreapta = merge_sort(lista[mijloc:])
        if stanga != None and dreapta != None:
            return unire(stanga, dreapta)
        else:
            return []
if __name__ == "__main__":
 # min_max_matrice()
 # matrice_generata()
 print(merge_sort([25, 1, 60, 3, 14, 9, 26, 5]))