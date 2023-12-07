"""
ADVENT OF CODE 2023 - DAY 7
Author: Michael Tezza
Date: 07/12/2023
Description: 
    Part 1: 
    In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.
    A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
    The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
    Every hand is exactly one type. From strongest to weakest, they are:

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
    Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

    If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand.
    If these cards are different, the hand with the stronger first card is considered stronger.
    If the first card in each hand have the same label, however, then move on to considering the second card in each hand.
    If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

    So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger.
    Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first 
    and second card).

    To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

            32T3K 765
            T55J5 684
            KK677 28
            KTJJT 220
            QQQJA 483
    This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, 
    where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands 
    in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

    So, the first step is to put the hands in order of strength:

    32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
    KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), 
    so KTJJT gets rank 2 and KK677 gets rank 3.
    T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
    Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with 
    its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

    Find the rank of every hand in your set. What are the total winnings?
"""
def magg(str1, str2):
    for i in range(5):
        if defLettera(str1[i]) < defLettera(str2[i]):
            return True
        if defLettera(str1[i]) > defLettera(str2[i]):
            return False
    return False

def insert(lista, elemento, n):
    lista1 = []
    if n != 0:
        for i in range(n):
            lista1.append(lista[i])
    #print("INSERT, prima: ", lista1)
    lista1.append(elemento)
    #print("INSERT, dopo: ", lista1)
    for i in range(n, len(lista)):
            lista1.append(lista[i])
    #print("INSERT, dopo2: ", lista1)
    return lista1

def defLettera(lettera):
    if lettera == "A":
        return 14
    elif lettera == "K":
        return 13
    elif lettera == "Q":
        return 12
    elif lettera == "J":
        return 11
    elif lettera == "T":
        return 10
    else:
        return int(lettera)

def Ordina(lista):
    #print("Lista da ordinare: ", lista)
    listao = []
    for a in lista:
        if len(listao) == 0:
            #print("Aggiunto", a)
            listao.append(a)
            #print("lista ordinata: ", listao)
        else:
            n = 0        
            aggiunto = False
            #print("listao: ", listao)
            for b in range(len(listao)):
                if magg(a[0], listao[b][0]):
                    #print("lista ordinata: ", listao)
                    listao = insert(listao, a, b)
                    #print("Aggiunto (con insert)", a)
                    #print("lista ordinata: ", listao)
                    aggiunto = True
                    break
                if aggiunto:
                    break
            if not aggiunto:
                listao.append(a)  
                #print("Aggiunto (con append)", a)   
                #print("lista ordinata: ", listao)        
    return listao

def FiveOfAKind(stringa):
    l = stringa[0]
    for i in stringa:
        if i != l:
            return False
    return True

def FourOfAKind(stringa):
    n1,n2 = 0,0
    l1 = stringa[0]
    l2 = stringa[1]
    for i in stringa:
        if i == l1:
            n1+=1
        elif i == l2:
            n2+=1
    if n1 == 4 or n2 == 4:
        return True
    return False

def Full(stringa):
    lista = {}
    for i in stringa:
        if i not in lista:
            lista[i] = 1
        else:
            lista[i]+=1
    #print(lista)
    
    if len(lista) == 2:
        for i in lista:
            if lista[i] == 3 or lista[i] == 2:
                return True
    return False
        
def Tris(stringa):
    lista = {}
    for i in stringa:
        if i not in lista:
            lista[i] = 1
        else:
            lista[i]+=1
    if len(lista) == 3:
        for i in lista:
            if lista[i] == 3:
                return True
    return False

def DoppiaCoppia(stringa):
    lista = {}
    for i in stringa:
        if i not in lista:
            lista[i] = 1
        else:
            lista[i]+=1
        
    if len(lista) == 3:
        lista = list(lista.values())
        if lista[0] == 2 and lista[1] == 2:
            return True
        if lista[0] == 2 and lista[2] == 2:
            return True
        if lista[1] == 2 and lista[2] == 2:
            return True
    return False

def Coppia(stringa):
    lista = {}
    for i in stringa:
        if i not in lista:
            lista[i] = 1
        else:
            lista[i]+=1
    if len(lista) == 4:
        for i in lista:
            if lista[i] == 2:
                return True
    return False

def CartaAlta(stringa):
    lista = []
    for i in stringa:
        if i not in lista:
            lista.append(i)
        else:
            return False
    return True
def Part1(filename):
    lista = []
    for i in open(filename):
        lista.append([i.strip().split(" ")[0], i.strip().split(" ")[1]])
    
    listaFive = []
    listaFour = []
    listaFull = []
    listaTris = []
    listaDoppiaCoppia = []
    listaCoppia = []
    listaCartaAlta = []
    for i in lista:
        if FiveOfAKind(i[0]):
            listaFive.append(i)
        elif FourOfAKind(i[0]):
            listaFour.append(i)
        elif Full(i[0]):
            listaFull.append(i)
        elif Tris(i[0]):
            listaTris.append(i)
        elif DoppiaCoppia(i[0]):
            listaDoppiaCoppia.append(i)
        elif Coppia(i[0]):
            listaCoppia.append(i)
        elif CartaAlta(i[0]):
            listaCartaAlta.append(i)
    print("Five of a kind: ", listaFive)
    listaFive = Ordina(listaFive)
    print("Five list ordinata: ",listaFive)
    print("-----------------------------------")
    print("Four of a kind: ", listaFour)
    listaFour = Ordina(listaFour)
    print("Four list ordinata: ",listaFour)
    print("-----------------------------------")
    print("Full: ", listaFull)
    listaFull = Ordina(listaFull)
    print("Full list ordinata: ",listaFull)
    print("-----------------------------------")
    print("Tris: ", listaTris)
    listaTris = Ordina(listaTris)
    print("Tris list ordinata: ",listaTris)
    print("-----------------------------------")
    print("Doppia coppia: ", listaDoppiaCoppia)
    listaDoppiaCoppia = Ordina(listaDoppiaCoppia)
    print("Doppia coppia list ordinata: ",listaDoppiaCoppia)
    print("-----------------------------------")
    print("Coppia: ", listaCoppia)
    listaCoppia = Ordina(listaCoppia)
    print("Coppia list ordinata: ",listaCoppia)
    print("-----------------------------------")
    print("Carta alta: ", listaCartaAlta)
    listaCartaAlta = Ordina(listaCartaAlta)
    print("Carta alta list ordinata: ",listaCartaAlta)
    print("-----------------------------------")
    n = 1
    tot = 0

    for i in listaCartaAlta:
        print(n, i)
        tot += int(i[1])*n
        n+=1

    for i in listaCoppia:
        print(n, i)
        tot += int(i[1])*n
        n+=1

    for i in listaDoppiaCoppia:
        print(n, i)
        tot += int(i[1])*n
        n+=1

    for i in listaTris:
        print(n, i)
        tot += int(i[1])*n
        n+=1

    for i in listaFull:
        print(n, i)
        tot += int(i[1])*n
        n+=1

    for i in listaFour:
        print(n, i)
        tot += int(i[1])*n
        n+=1

    for i in listaFive:
        print(n, i)
        tot += int(i[1])*n
        n+=1
        
    print(tot)

if __name__ == "__main__":
    Part1("./Advent7/input.txt")