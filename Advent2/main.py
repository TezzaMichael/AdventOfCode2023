def Part1(filename):
    id = 1
    tot_id = 0
    n = ""
    flag = True
    for row in open(filename):
        #12 red cubes, 13 green cubes, and 14 blue cubes
        row = row.split(":")[1]
        lista1 = row.split(";")
        for i in range(len(lista1)):
            for l in range(len(lista1[i])):
                if lista1[i][l] in "0123456789":
                    n+=lista1[i][l]
                if lista1[i][l] == "b" and lista1[i][l+1] == "l" and lista1[i][l+2] == "u" and lista1[i][l+3] == "e":
                    if int(n) > 14:
                        flag = False
                    n = ""
                if lista1[i][l] == "r" and lista1[i][l+1] == "e" and lista1[i][l+2] == "d":
                    if int(n) > 12:
                        flag = False
                    n = ""
                if lista1[i][l] == "g" and lista1[i][l+1] == "r" and lista1[i][l+2] == "e" and lista1[i][l+3] == "e" and lista1[i][l+4] == "n":
                    if int(n) > 13:
                        flag = False
                    n = ""
        """if red < 12 and blue < 14 and green < 13:
            tot_id += id"""
        if flag:
            #print(id)
            tot_id += id
        id += 1
        n = ""
        flag = True
                
    print(tot_id)

def Part2(filename):
    id = 1
    tot = 0
    power = 0
    n = ""
    red = 0
    green = 0
    blue = 0
    for row in open(filename):
        #12 red cubes, 13 green cubes, and 14 blue cubes
        row = row.split(":")[1]
        lista1 = row.split(";")
        for i in range(len(lista1)):
            for l in range(len(lista1[i])):
                if lista1[i][l] in "0123456789":
                    n+=lista1[i][l]
                if lista1[i][l] == "b" and lista1[i][l+1] == "l" and lista1[i][l+2] == "u" and lista1[i][l+3] == "e":
                    if int(n) > blue:
                        blue = int(n)
                    n = ""
                if lista1[i][l] == "r" and lista1[i][l+1] == "e" and lista1[i][l+2] == "d":
                    if int(n) > red:
                        red = int(n)
                    n = ""
                if lista1[i][l] == "g" and lista1[i][l+1] == "r" and lista1[i][l+2] == "e" and lista1[i][l+3] == "e" and lista1[i][l+4] == "n":
                    if int(n) > green:
                        green = int(n)
                    n = ""
        power = red * green * blue
        tot += power
        id += 1
        n = ""
        red = 0
        green = 0
        blue = 0
                
    print(tot)
if __name__ == "__main__":
    #Part1("./Advent2/input.txt")
    Part2("./Advent2/input.txt")