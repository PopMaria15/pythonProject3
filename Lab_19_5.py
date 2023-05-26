graph = [[0, 1], [0, 2],
         [1, 2], [1, 3],
         [2, 4], [2, 6],
         [4, 5], [4, 8],
         [5, 7]]
adancime = 0
inainte = []
dupa = []

def parcurgeregraph(graph, start, adancime):
    if start not in inainte:
        dupa.append(start)
        for element in graph:
            if element[0] == start and start not in inainte:
                inainte.append(start)
                parcurgeregraph(graph, element[1], adancime+1)

def parcurgeregraphiterativ(graph, start):
    cale = []
    nodcurent = start
    cale.append(nodcurent)
    for element in graph:
        if element[0] == nodcurent:
             nodcurent = element[1]
             cale.append(nodcurent)
    return cale

def toatecaile(graph):
    n = len(graph)
    i = 0
    while i < n:
        primelement = graph[0][0]
        print(parcurgeregraphiterativ(graph, primelement))
        graph.pop(0)
        i += 1


if __name__ == "__main__":
 # parcurgeregraph(graph, 0, 1)
 # print(inainte)
 # print(dupa)
 # print(parcurgeregraphiterativ(graph, 0))
 toatecaile(graph)
