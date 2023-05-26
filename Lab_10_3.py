def tehnica_greedy(lista_timpi_reparatie):
    timp = int(input("Introduceti numarul de ore de lucru: "))
    masini_reparate = []
    lista_timpi_reparatie_sortata = sorted(lista_timpi_reparatie)
    for i in range(len(lista_timpi_reparatie_sortata)):
        if lista_timpi_reparatie_sortata[i] <= timp:
            timp -= lista_timpi_reparatie_sortata[i]
            masini_reparate.append(lista_timpi_reparatie_sortata[i])
    print(masini_reparate)


def tehnica_greedy2(lista_timpi_reparatie):
    timp = int(input("Introduceti numarul de ore de lucru: "))
    masini_reparate = []
    lista_timpi_reparatie_sortata = sorted(lista_timpi_reparatie)
    i = 0
    while i <= len(lista_timpi_reparatie_sortata) and timp >= 0:
        if lista_timpi_reparatie_sortata[i] <= timp:
            timp -= lista_timpi_reparatie_sortata[i]
            masini_reparate.append(lista_timpi_reparatie_sortata[i])
            i += 1
    print(masini_reparate)


def suma(n):
    if n == 0:
        return 0
    else:
        return suma(n-1)+n


def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return suma_lista(lista[:len(lista) - 1]) + lista[len(lista) - 1]


def suma_lista_divideetimpera(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        mijloc = len(lista) // 2
        return suma_lista_divideetimpera(lista[:mijloc]) +suma_lista_divideetimpera(lista[mijloc:])

if __name__ == "__main__":
 # tehnica_greedy([1, 5, 20, 1, 3, 300])
 # tehnica_greedy2([1, 5, 20, 1, 3, 300])
 # print(suma(10))
 # print(suma_lista([4, 1, 8, 4, 3, 5, 10]))
 # print(suma_lista_divideetimpera([4, 1, 8, 4, 3, 5, 10]))
 print(suma_lista_divideetimpera([2, 3, 5, 1, 200, 100, 40]))