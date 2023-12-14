"""
ADVENT OF CODE 2023 - DAY 11
Author: Michael Tezza
Date: 14/12/2023
"""
def parse(filename):
    lista = []
    for i in open(filename):
        lista1 = []
        for a in i.strip():
            lista1.append(a)
        lista.append(lista1)
    return lista

def find_universe(lista):
    universe = []
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if lista[i][a] == "#":
                universe.append([i, a])
    print(len(universe))
    return universe

def find_empty_xy(lista):
    emptyx = []
    emptyy = []
    for i in range(len(lista)):
        update = True
        for a in range(len(lista[i])):
            if lista[i][a] == "#":
                update = False
        if update:
            emptyx.append(i)
    for i in range(len(lista[0])):
        update = True
        for a in range(len(lista)):
            if lista[a][i] == "#":
                update = False
        if update:
            emptyy.append(i)
    
    return emptyx, emptyy

def calc_track(pos1, pos2, emptyx, emptyy):
    n = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    for i in emptyx:
        if pos1[0] < i < pos2[0] or pos2[0] < i < pos1[0]:
            n+=1
    for i in emptyy:
        if pos1[1] < i < pos2[1] or pos2[1] < i < pos1[1]:
            n+=1
    return n

def calc_track2(pos1, pos2, emptyx, emptyy):
    n = abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
    n1 = 0
    for i in emptyx:
        if pos1[0] < i < pos2[0] or pos2[0] < i < pos1[0]:
            n1+=1
    for i in emptyy:
        if pos1[1] < i < pos2[1] or pos2[1] < i < pos1[1]:
            n1+=1
    return n + (n1*(1000000-1))

def Part1(filename):
    n = 0
    lista = parse(filename)
    universe = find_universe(lista)
    emptyx, emptyy = find_empty_xy(lista)
    #print(universe)
    for i in range(len(universe)):
        for a in range(i, len(universe)):
            n+=calc_track(universe[i], universe[a], emptyx, emptyy)
    print(n)

def Part2(filename):
    n = 0
    lista = parse(filename)
    universe = find_universe(lista)
    emptyx, emptyy = find_empty_xy(lista)
    #print(universe)
    for i in range(len(universe)):
        for a in range(i, len(universe)):
            n+=calc_track2(universe[i], universe[a], emptyx, emptyy)
    print(n)


if __name__ == "__main__":
    Part1("Advent11/input.txt")
    Part2("Advent11/input.txt")
