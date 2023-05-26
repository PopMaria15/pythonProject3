def change():
    suma_plata = int(input("Introduceti bancnota cu care se plateste: "))
    suma_produse = int(input("Introduceti valoarea produselor: "))
    lista = [1, 5, 10, 20, 50, 100]
    change = suma_plata - suma_produse
    lista.reverse()
    lista_indici = [0]*len(lista)
    for i in range(len(lista)):
        while change >= lista[i]:
            change -= lista[i]
            lista_indici[i] += 1
    for elem in range(len(lista)):
        print(str(lista_indici[elem]) + " bucati de " + str(lista[elem]))
    print(" ")


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_lista():
    n = int(input("Introduceti un numar natural n: "))
    if n <= 2:
       return 1
    lista_fibonacci = [0] * n
    lista_fibonacci[0] = 0
    lista_fibonacci[1] = 1
    for i in range(2, n):
        lista_fibonacci[i] = lista_fibonacci[i-1] + lista_fibonacci[i-2]
    return lista_fibonacci

if __name__ == "__main__":
 # change()
 # print(fibonacci(10))
 print(fibonacci_lista())