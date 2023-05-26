import random


def maxim_lista(lista):
    max_value = 0
    for elem in lista:
        for elem2 in elem:
            if elem2 > max_value:
                max_value = elem2
    return max_value + 1


def creare_matrice(lista):
    matrix = [[0] * n for _ in range(n)]
    for elem in lista:
        x = elem[0]
        y = elem[1]
         matrix[x][y] = 1
         matrix[y][x] = 1
    return matrix


def generare_lista(matrice):
    l = []
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1 and i > j:
                l.append([i, j])


def printare_matrice(matrix, lungime_lista):
    for i in range(lungime_lista):
        for j in range(lungime_lista):
        print(matrix[i][j], end=" ")
    print("\n")


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        return 1
    else:
        return 0


if __name__ == "__main__":
    n = maxim_lista([[0, 1], [0, 2], [1, 3], [3, 4], [1, 2]])
    matrice = creare_matrice([[0, 1], [0, 2], [1, 3], [3, 4], [1, 2]])
    # printare_matrice(matrice, n)
    # print(generare_lista(matrice))
     v = 0
     for i in range(100):
         v += roll_dice()
    print(v/100)
    v = 0
    for i in range(1000):
        v += roll_dice()
 print(v / 1000)
 v = 0
 for i in range(10000):
    v += roll_dice()
 print(v / 10000)
