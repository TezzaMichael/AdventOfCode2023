"""
ADVENT OF CODE 2023 - DAY 10
Author: Michael Tezza
Date: 14/12/2023
"""
import time

def parse(filename):
    lista = []
    for i in open(filename):
        lista1 = []
        for a in i.strip():
            lista1.append(a)
        lista.append(lista1)
    return lista



def start(lista):
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if lista[i][a] == "S":
                return i, a


def direction(lista, pos_act, pos_pre):
    print("SIMB0LO:", lista[pos_act[0]][pos_act[1]])
    if lista[pos_act[0]][pos_act[1]] == "|" :
        if pos_act[0] > pos_pre[0] and pos_act[0] < len(lista):
            return [pos_act[0]+1, pos_act[1]], pos_act
        elif pos_act[0] >= 1:
            return [pos_act[0]-1, pos_act[1]], pos_act
        else:
            return None, None
    elif lista[pos_act[0]][pos_act[1]] == "-":
        if pos_act[1] > pos_pre[1] and pos_act[1] < len(lista[0]):
            return [pos_act[0], pos_act[1]+1], pos_act
        elif pos_act[1] >= 1:
            return [pos_act[0], pos_act[1]-1], pos_act
        else:
            return None, None
    elif lista[pos_act[0]][pos_act[1]] == "L":
        if pos_act[0] > pos_pre[0] and pos_act[1] < len(lista[0]):
            return [pos_act[0], pos_act[1]+1], pos_act
        elif pos_act[0] >= 1:
            return [pos_act[0]-1, pos_act[1]], pos_act
        else:
            return None, None
    elif lista[pos_act[0]][pos_act[1]] == "J":
        if pos_act[0] > pos_pre[0] and pos_act[0] >= -1:
            return [pos_act[0], pos_act[1]-1], pos_act
        elif pos_act[0] >= 1:
            return [pos_act[0]-1, pos_act[1]], pos_act
        else:
            return None, None
    elif lista[pos_act[0]][pos_act[1]] == "7":
        if pos_act[0] < pos_pre[0] and pos_act[0] >= -1:
            return [pos_act[0], pos_act[1]-1], pos_act
        elif pos_act[0] < len(lista):
            return [pos_act[0]+1, pos_act[1]], pos_act
        else:
            return None, None
    elif lista[pos_act[0]][pos_act[1]] == "F":
        #print("Decision:",pos_act, pos_pre)
        if pos_act[0] < pos_pre[0] and pos_act[1] < len(lista[0]):
            #print("entrato")
            return [pos_act[0], pos_act[1]+1], pos_act
        elif pos_act[0] < len(lista):
            return [pos_act[0]+1, pos_act[1]], pos_act
        else:
            return None, None
    else:
        return None, None

def Part1(filename):
    lista = parse(filename)
    x, y = start(lista)
    pos_pre = [[x, y], [x, y], [x, y], [x, y]]
    pos_act = []
    if x+1 < len(lista):
        pos_act.append([x+1, y])
    if x-1 >= 0:
        pos_act.append([x-1, y])
    if y+1 < len(lista[0]):
        pos_act.append([x, y+1])
    if y-1 >= 0:
        pos_act.append([x, y-1])

    n = 1
    while True:
        print("--------", n, "--------")
        first = pos_act[0]
        same = True
        for i in pos_act:
            if i[0] != first[0] or i[1] != first[1]:
                same = False
        if same:
            return n
        
        for i in range(len(pos_act)):
            print(pos_act[i], pos_pre[i], "--->", end=" ")
            print(direction(lista, pos_act[i], pos_pre[i]))
            pos_act[i], pos_pre[i] = direction(lista, pos_act[i], pos_pre[i])
        n += 1
        for i in pos_act:
            if i == None:
                pos_act.remove(i)
                pos_pre.remove(i)
        #time.sleep(5)
        print("Solution:", n/2)
        
def Part2(filename):
    n = 0
    lista = parse(filename)
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if i == 0 or i == len(lista)-1 or a == 0 or a == len(lista[i])-1:
                pass
            else:
                if lista[i][a] == ".":
                    count = 0
                    wait = False
                    wait1 = False
                    for c in range(i):
                        if lista[c][a] == "-" or lista[c][a] == "F" or lista[c][a] == "7" or lista[c][a] == "J" or lista[c][a] == "L" : 
                            count += 1
                        if lista[c][a] == "7":
                            wait = True
                        if lista[c][a] == "F":
                            wait1 = True
                        if wait and lista[c][a] == "J" or lista[c][a] == "L":
                            count -= 1
                            wait = False
                        if wait1 and lista[c][a] == "L" or lista[c][a] == "J":
                            count -= 1
                            wait1 = False
                    count1 = 0
                    wait = False
                    wait1 = False
                    for c in range(a):
                        if lista[i][c] == "|" or lista[i][c] == "F" or lista[i][c] == "7" or lista[i][c] == "J" or lista[i][c] == "L" : 
                            count1 += 1
                        if lista[c][a] == "L":
                            wait = True
                        if lista[c][a] == "F":
                            wait1 = True
                        if wait and lista[c][a] == "7" or lista[c][a] == "J":
                            count -= 1
                            wait = False
                        if wait1 and lista[c][a] == "7" or lista[c][a] == "J":
                            count -= 1
                            wait1 = False
                    if count%2 != 0 and count1%2 != 0:
                        n += 1
    print("Part 2:", n*2 +1)
if __name__ == "__main__":
    Part1("./Advent10/input.txt")
    #Part2("./Advent10/input.txt")