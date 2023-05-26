def cautare_lista(lista, elem):
    k = 0
    for i in range(len(lista)):
        if lista[i] == elem:
            k = 1
    if k == 1:
         print("Gasit!")
    else:
        print("Nu exista!")


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        index_valoare_minima = i
        for j in range(i+1, n):
            if lista[j] < lista[index_valoare_minima]:
             index_valoare_minima = j
        if index_valoare_minima != i:
            lista[index_valoare_minima], lista[i] = lista[i],lista[index_valoare_minima]
    return lista


def angajati(lista, id_cautat):
    for i in range(len(lista)):
        if lista[i]["id"] == id_cautat:
            print(lista[i]["age"])

if __name__ == "__main__":
    a1 = {"id": 14, "name": "john doe", "age": 36, "position": "Business Manager"}
    a2 = {"id": 2, "name": "vasile", "age": 21, "position": "n/a"}
    a3 = {"id": 110, "name": "john smith", "age": 50, "position": "engineer"}
    a4 = {"id": 40, "name": "cristi", "age": 18, "position": "programator"}
    # cautare_lista([1, 2, 3, 4, 5], 2)
    # print(selection_sort([20, 12, 10, 15, 2]))
    angajati([a1, a2, a3, a4], 14)