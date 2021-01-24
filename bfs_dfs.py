

import copy


class node:
    def __init__(self, estado, pai, movimento):
        self.estado = copy.deepcopy(estado)
        self.pai = pai
        self.movimento = movimento


estadoFinal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
estadoInicial = [[0, 1, 3], [6, 8, 2], [7, 5, 4]]


def swap(l, c, nl, nc, estado):
    aux = estado[l][c]
    estado[l][c] = estado[nl][nc]
    estado[nl][nc] = aux


def bfs():
    estados = [copy.deepcopy(estadoInicial)]
    nos = [node(estadoInicial, None, None)]
    cont = 0
    movimentos = []
    while True:

        estadoAtual = copy.deepcopy(estados[cont])
        if estadoAtual == estadoFinal:
            no = nos[cont]
            while no.pai is not None:
                movimentos.insert(0, no.movimento)
                no = no.pai

            print("quantidade de nos expandidos: ", len(estados))
            return movimentos

        for i in range(3):
            for j in range(3):
                if estadoAtual[i][j] == 0:
                    zeroCoord = [i, j]

        # vai pra esquerda
        if zeroCoord[1] > 0:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0], zeroCoord[1] - 1, estadoAux)
            if estadoAux not in estados:
                nos.append(node(estadoAux, nos[cont], "esquerda"))
                estados.append(estadoAux)

        # vai pra direita
        if zeroCoord[1] < 2:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0], zeroCoord[1] + 1, estadoAux)
            if estadoAux not in estados:
                nos.append(node(estadoAux, nos[cont], "direita"))
                estados.append(estadoAux)

        # vai pra cima
        if zeroCoord[0] > 0:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0] - 1, zeroCoord[1], estadoAux)
            if estadoAux not in estados:
                nos.append(node(estadoAux, nos[cont], "cima"))
                estados.append(estadoAux)

        # vai pra baixo
        if zeroCoord[0] < 2:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0] + 1, zeroCoord[1], estadoAux)
            if estadoAux not in estados:
                nos.append(node(estadoAux, nos[cont], "baixo"))
                estados.append(estadoAux)

        cont += 1


def dfs():
    estados = [copy.deepcopy(estadoInicial)]
    nos = [node(estadoInicial, None, None)]
    cont = 0
    nivel = 0
    movimentos = []
    while True:

        if nivel == 50:
            aux = estados.pop(cont)
            estados.append(aux)
            noaux = nos.pop(cont)
            nos.append(noaux)
            nivel -= 1

        estadoAtual = copy.deepcopy(estados[cont])

        if estadoAtual == estadoFinal:
            no = nos[cont]
            while no.pai is not None:
                movimentos.insert(0, no.movimento)
                no = no.pai
            print("quantidade de nos expandidos: ", len(estados))
            return movimentos

        for i in range(3):
            for j in range(3):
                if estadoAtual[i][j] == 0:
                    zeroCoord = [i, j]

        # vai pra esquerda
        if zeroCoord[1] > 0:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0], zeroCoord[1] - 1, estadoAux)
            if estadoAux not in estados:
                estados.insert(cont, estadoAux)
                nos.insert(cont, node(estadoAux, nos[cont], "esquerda"))
                nivel += 1
                continue

        # vai pra direita
        if zeroCoord[1] < 2:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0], zeroCoord[1] + 1, estadoAux)
            if estadoAux not in estados:
                estados.insert(cont, estadoAux)
                nos.insert(cont, node(estadoAux, nos[cont], "direita"))
                nivel += 1
                continue

        #vai pra cima
        if zeroCoord[0] > 0:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0] - 1, zeroCoord[1], estadoAux)
            if estadoAux not in estados:
                estados.insert(cont, estadoAux)
                nos.insert(cont, node(estadoAux, nos[cont], "cima"))
                nivel += 1
                continue

        #vai pra baixo
        if zeroCoord[0] < 2:
            estadoAux = copy.deepcopy(estadoAtual)
            swap(zeroCoord[0], zeroCoord[1], zeroCoord[0] + 1, zeroCoord[1], estadoAux)
            if estadoAux not in estados:
                estados.insert(cont, estadoAux)
                nos.insert(cont, node(estadoAux, nos[cont], "baixo"))
                nivel += 1
                continue

        cont += 1
        nivel -= 1

a = int(input("digite 1 para busca em largura ou 2 para busca em profundidade\n"))

if a == 1:
    movimentos = bfs()
    print("quantidade de movimentos: ", len(movimentos))
    print(movimentos)
if a == 2:
    movimentos = dfs()
    print("quantidade de movimentos: ", len(movimentos))
    print(movimentos)













