import random

def cautare(lista, nr_cautat):
    for i in range(len(lista)):
        if lista[i] == nr_cautat:
            return i
    return -1


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
    return array


def generareCNP(gen, an, luna, zi, judet, nnn):
    CNP = ""
    #S
    if gen in ("m", "M", "masculin", "MASCULIN", "barbat", "BARBAT"):
        if an < 2000:
            CNP += "1"
        else:
            CNP += "5"
    else:
        if an < 2000:
            CNP += "2"
        else:
            CNP += "6"
    if an < 2000:
        an -= 1900
    else:
        an -= 2000
     #AA
    if an < 10:
        CNP += "0"
    CNP += str(an)
    #LL
    if luna < 10:
        CNP += "0"
    CNP += str(luna)
    #ZZ
    if zi < 10:
        CNP += "0"
    CNP += str(zi)
    #JJ
    if judet < 10:
        CNP += "0"
    CNP += str(judet)
    #NNN
    if nnn<10:
        CNP += "00"
    elif nnn < 100:
        CNP += "0"
    CNP += str(nnn)
    # C
    CNP += str(generareC(CNP))
    return CNP


def generareC(sir):
    sir_control = "279146358279"
    suma = 0
    for i in range(len(sir)):
        suma += int(sir[i]) * int(sir_control[i])
    if suma % 11 == 10:
        return 1
    else:
        return suma % 11

if __name__ == "__main__":
    ht = {}
    gen = "M"
    for i in range(1000):
        an = random.randint(1900, 2023)
        luna = random.randint(1, 12)
        zi = random.randint(1, 28)
        judet = random.randint(1, 40)
        nnn = random.randint(1, 999)
        cnp = generareCNP(gen, an, luna, zi, judet, nnn)
        ht[cnp] = i
        print(insertionSort([1, 9, 3, 5, 4]))