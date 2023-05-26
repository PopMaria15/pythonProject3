# determinati minimul si maximul dintr-o lista primita ca parametru


def min_max(lista):
    minim = 999999
    maxim = 0
    for i in range(len(lista)):
        if lista[i] > maxim:
            maxim = lista[i]
        if lista[i] < minim:
            minim = lista[i]
    return minim, maxim
    # print(minim)
    # print(maxim)


def min_max_sort(lista):
    lista.sort()
    minim1 = lista[0]
    minim2 = lista[1]
    maxim1 = lista[len(lista)-1]
    maxim2 = lista[len(lista)-2]
    print(minim1, minim2, maxim1, maxim2)


def min_max_math(lista):
    minim = min(lista)
    maxim = max(lista)
    print(minim)
    print(maxim)


def parcurgere_matrice(matrice):
    n = len(matrice)
    sir = "abcd"
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1:
                print(sir[i], sir[j], end=" ")
        print(" ")


def aparitii_zero(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + aparitii_zero(n//10)
    else:
        return aparitii_zero(n//10)


if __name__ == "__main__":
 # print(min_max([20, 45485, 0, 7235, 4]))
 # min_max_sort([20, 45485, 0, 7235, 4])
 # min_max_math([20, 45485, 0, 7235, 4])
 # parcurgere_matrice([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0,0]])
 print(aparitii_zero(100200000))