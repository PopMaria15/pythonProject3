def cautare_numar_in_lista(lista, n):
    sw = 0
    for elem in lista:
        if elem == n:
            sw = 1
    if sw == 1:
        return True
    else:
        return False


def cautare_numar_in_matrice(matrice, n):
    sw = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
             if matrice[i][j] == n:
                 sw = 1
    if sw == 1:
        return True
    else:
        return False


def factorial(n):
    if n <= 0:
        return "Nu exista"
    if n == 1:
        return 1
    return n * factorial(n-1)


def suma_cifrelor(n):
    if n <= 0:
        return 0
    return n % 10 + suma_cifrelor(n // 10)


def bubble_sort(lista):
    flg = 1
    while flg == 1:
        flg = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                flg = 1
    return lista

if __name__ == "__main__":
 # print(cautare_numar_in_lista([1, 2, 3, 4, 5], 3))
 # print(cautare_numar_in_matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25))
 # print(factorial(3))
 # print(suma_cifrelor(1234))
 print(bubble_sort([2, 5, 4, 3, 7]))