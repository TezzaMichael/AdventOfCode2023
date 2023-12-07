"""
ADVENT OF CODE 2023 - DAY 7
Author: Michael Tezza
Date: 07/12/2023
Description: 
    Part 2: 
    To make things a little more interesting, the Elf introduces one additional rule. 
    Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

    To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay 
    in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

    J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. 
    However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, 
    not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

    Now, the above example goes very differently:

            32T3K 765
            T55J5 684
            KK677 28
            KTJJT 220
            QQQJA 483
    32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
    KK677 is now the only two pair, making it the second-weakest hand.
    T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
    With the new joker rule, the total winnings in this example are 5905.

    Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
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
        return 1
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
    if 'J' in stringa :
        lista = {}
        for i in stringa:
            if i not in lista:
                lista[i] = 1
            else:
                lista[i]+=1
        if len(lista) <= 2:
            return True
        return False
    else:
        l = stringa[0]
        for i in stringa:
            if i != l:
                return False
        return True

def FourOfAKind(stringa):
    if 'J' in stringa :
        lista = {}
        for i in stringa:
            if i not in lista:
                lista[i] = 1
            else:
                lista[i]+=1
        
        if len(lista) == 3:
            if lista['J'] == 1:
                for i in lista:
                    if i != 'J' and lista[i] == 3 or i == 'J' and lista[i] == 1:
                        return True
                return False
            if lista['J'] == 2:
                for i in lista:
                    if i != 'J' and lista[i] == 1 or i == 'J' and lista[i] == 2:
                        return True
                return False
            if lista['J'] == 3:
                for i in lista:
                    if i != 'J' and lista[i] == 1:
                        return True
                return False
            return True
        else:
            return False
    else:
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
    if 'J' in stringa :
        lista = {}
        for i in stringa:
            if i not in lista:
                lista[i] = 1
            else:
                lista[i]+=1
        if len(lista) == 3:
            if lista['J'] == 1:
                for i in lista:
                    if i != 'J' and lista[i] == 2 :
                        return True
                return False
            return False
        return False
        
    else:
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
    if 'J' in stringa :
        lista = {}
        for i in stringa:
            if i not in lista:
                lista[i] = 1
            else:
                lista[i]+=1
        if len(lista) == 4:
            if lista['J'] == 1:
                for i in lista:
                    if i != 'J' and lista[i] == 1 or i != 'J' and lista[i] == 2 :
                        return True
                return False
            if lista['J'] == 2:
                for i in lista:
                    if i != 'J' and lista[i] == 1 :
                        return True
                return False
            return False
        return False
    
    else:
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
    if 'J' in stringa :
        return False
    else:
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
    if 'J' in stringa:
        lista = {}
        for i in stringa:
            if i not in lista:
                lista[i] = 1
            else:
                lista[i]+=1
        if len(lista) == 5:
            return True
        return False
    else:    
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
    if 'J' in stringa :
        return False
    else:
        lista = []
        for i in stringa:
            if i not in lista:
                lista.append(i)
            else:
                return False
        return True
def Part2(filename):
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
    file = open("output.txt", "w")
    print("Carta Alta: ")
    for i in listaCartaAlta:
        print(n, i)
        tot += int(i[1])*n
        n+=1
    print("Coppia: ")
    for i in listaCoppia:
        print(n, i)
        for o in i[0]:
            if o == 'J':
                file.write(str(i[0])+"\n")
        #file.write(str(i[0])+"\n")
        tot += int(i[1])*n
        n+=1
    print("Doppia Coppia: ")
    for i in listaDoppiaCoppia:
        print(n, i)
        #file.write(str(i[0])+"\n")
        tot += int(i[1])*n
        n+=1
    print("Tris: ")
    for i in listaTris:
        print(n, i)
        #file.write(str(i[0])+"\n")
        tot += int(i[1])*n
        n+=1
    print("Full: ")
    for i in listaFull:
        print(n, i)
        #file.write(str(i[0])+"\n")
        tot += int(i[1])*n
        n+=1
    print("Four: ")
    for i in listaFour:
        print(n, i)
        #file.write(str(i[0])+"\n")
        tot += int(i[1])*n
        n+=1
    print("Five: ")
    for i in listaFive:
        print(n, i)
        #file.write(str(i[0])+"\n")
        tot += int(i[1])*n
        n+=1
    file.close()
    print(tot)

if __name__ == "__main__":
    Part2("./Advent7/input-example.txt")