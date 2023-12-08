"""
ADVENT OF CODE 2023 - DAY 8
Author: Michael Tezza
Date: 08/12/2023
Description: 
    Part 1: 
        It seems like you're meant to use the left/right instructions to navigate the network. 
        Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

        After examining the maps for a bit, two nodes stick out: AAA and ZZZ. 
        You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

        This format defines each node of the network individually. For example:

                RL

                AAA = (BBB, CCC)
                BBB = (DDD, EEE)
                CCC = (ZZZ, GGG)
                DDD = (DDD, DDD)
                EEE = (EEE, EEE)
                GGG = (GGG, GGG)
                ZZZ = (ZZZ, ZZZ)
        Starting with AAA, you need to look up the next element based on the next left/right instruction in your input.
        In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC.
        Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

        Of course, you might not find ZZZ right away.
        If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on.
        For example, here is a situation that takes 6 steps to reach ZZZ:

                LLR

                AAA = (BBB, BBB)
                BBB = (AAA, ZZZ)
                ZZZ = (ZZZ, ZZZ)
        Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
    Part 2:
        After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z!
        If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

        For example:

                LR

                11A = (11B, XXX)
                11B = (XXX, 11Z)
                11Z = (11B, XXX)
                22A = (22B, XXX)
                22B = (22C, 22C)
                22C = (22Z, 22Z)
                22Z = (22B, 22B)
                XXX = (XXX, XXX)
        Here, there are two starting nodes, 11A and 22A (because they both end with A). 
        As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on.
        Repeat this process until all of the nodes you're currently on end with Z.
        (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.)
        In this example, you would proceed as follows:

                Step 0: You are at 11A and 22A.
                Step 1: You choose all of the left paths, leading you to 11B and 22B.
                Step 2: You choose all of the right paths, leading you to 11Z and 22C.
                Step 3: You choose all of the left paths, leading you to 11B and 22Z.
                Step 4: You choose all of the right paths, leading you to 11Z and 22B.
                Step 5: You choose all of the left paths, leading you to 11B and 22C.
                Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
        So, in this example, you end up entirely on nodes that end in Z after 6 steps.

        Simultaneously start on every node that ends with A. 
        How many steps does it take before you're only on nodes that end with Z?
"""
def parse(filename):
    firstRow = True
    istructions = []
    lista = {}
    for i in open(filename):
        if firstRow:
            firstRow = False
            for i in i.strip():
                istructions.append(i)
        elif i == "\n":
            pass
        else:
            lista[i.split(" =")[0]] = [i.split("= (")[1].split(",")[0], i.split(", ")[1].split(")")[0]]
    #print(lista)
    return istructions, lista

def Part1(filename):
    instructions, lista = parse(filename)
    n = 0
    act = 'AAA'
    while(True):
        for i in instructions:
            if act == 'ZZZ':
                print(act, n)
                return n
            if i == "L":
                print(act, n)
                act = lista[act][0]
                n+=1
            else:
                print(act, n)
                act = lista[act][1]
                n+=1

def Part2(filename):
    instructions, lista = parse(filename)
    listaA = []
    for i in lista:
        if i[2] == 'A':
            listaA.append(i)
    n = 0
    while(True):
        for i in instructions:
            for a in range(len(listaA)):
                #print(listaA[a], n)
                if i == "L":
                    print(listaA[a], n)
                    listaA[a] = lista[listaA[a]][0]
                else:
                    print(listaA[a], n)
                    listaA[a] = lista[listaA[a]][1]
            n+=1
            print("----------------")
            victory = True
            for a in listaA:
                if a[2] != 'Z':
                    victory = False
            if victory:
                return n

if __name__ == "__main__":
    #print(Part1("Advent8/input-example.txt"))
    #print(Part1("Advent8/input.txt"))
    print(Part2("Advent8/input.txt"))