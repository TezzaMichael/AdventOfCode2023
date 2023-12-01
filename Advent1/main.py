def Part1(filename):
    string = ""
    num = ''
    tot = 0
    flag_1 = False
    for row in open(filename):
        print(row)
        for i in row:
            if i in "0123456789":
                if not flag_1:
                    string += i
                    flag_1 = True
                else:
                    num = i
        string += num
        if len(string) == 1:
            string+=string
        print(string)
        tot += int(string)
        string = ""
        num = ''
        flag_1 = False
    print(tot)
        
def Part2(filename):
    string = ""
    num = ''
    tot = 0
    flag_1 = False
    for row in open(filename):
        for i in range(len(row)):
            try:
                if row[i] == 'o' and row[i+1] == 'n' and row[i+2] == 'e':
                    if not flag_1:
                        string += '1'
                        flag_1 = True
                    else:
                        num = '1'
                elif row[i] == 't' and row[i+1] == 'w' and row[i+2] == 'o':
                    if not flag_1:
                        string += '2'
                        flag_1 = True
                    else:
                        num = '2'
                elif row[i] == 't' and row[i+1] == 'h' and row[i+2] == 'r' and row[i+3] == 'e' and row[i+4] == 'e':
                    if not flag_1:
                        string += '3'
                        flag_1 = True
                    else:
                        num = '3'
                elif row[i] == 'f' and row[i+1] == 'o' and row[i+2] == 'u' and row[i+3] == 'r':
                    if not flag_1:
                        string += '4'
                        flag_1 = True
                    else:
                        num = '4'
                elif row[i] == 'f' and row[i+1] == 'i' and row[i+2] == 'v' and row[i+3] == 'e':
                    if not flag_1:
                        string += '5'
                        flag_1 = True
                    else:
                        num = '5'
                elif row[i] == 's' and row[i+1] == 'i' and row[i+2] == 'x':
                    if not flag_1:
                        string += '6'
                        flag_1 = True
                    else:
                        num = '6'
                elif row[i] == 's' and row[i+1] == 'e' and row[i+2] == 'v' and row[i+3] == 'e' and row[i+4] == 'n':
                    if not flag_1:
                        string += '7'
                        flag_1 = True
                    else:
                        num = '7'
                elif row[i] == 'e' and row[i+1] == 'i' and row[i+2] == 'g' and row[i+3] == 'h' and row[i+4] == 't':
                    if not flag_1:
                        string += '8'
                        flag_1 = True
                    else:
                        num = '8'
                elif row[i] == 'n' and row[i+1] == 'i' and row[i+2] == 'n' and row[i+3] == 'e':
                    if not flag_1:
                        string += '9'
                        flag_1 = True
                    else:
                        num = '9'
                elif row[i] in "0123456789":
                    if not flag_1:
                        string += row[i]
                        flag_1 = True
                    else:
                        num = row[i]
            except:
                pass
        string += num
        if len(string) == 1:
            string+=string
        print(string)
        tot += int(string)
        string = ""
        num = ''
        flag_1 = False
    print(tot)

if __name__ == "__main__":
    #Part1('./Advent1/input-example.txt')    
    #Part1('./Advent1/input.txt')
    #Part2('./Advent1/input2-example.txt')
    Part2('./Advent1/input.txt')