"""
ADVENT OF CODE 2023 - DAY 9
Author: Michael Tezza
Date: 09/12/2023
Description: 
    Part 1: 
        In the above dataset, the first history is 0 3 6 9 12 15.
        Because the values increase by 3 each step, the first sequence of differences that you generate will be 3 3 3 3 3.
        Note that this sequence has one fewer value than the input sequence because at each step it considers two numbers from the input.
        Since these values aren't all zero, repeat the process: the values differ by 0 at each step, so the next sequence is 0 0 0 0.
        This means you have enough information to extrapolate the history! Visually, these sequences can be arranged like this:

                0   3   6   9  12  15
                3   3   3   3   3
                    0   0   0   0
        To extrapolate, start by adding a new zero to the end of your list of zeroes; because the zeroes represent differences between the two values above them,
        this also means there is now a placeholder in every sequence above it:

                0   3   6   9  12  15   B
                3   3   3   3   3   A
                    0   0   0   0   0
        You can then start filling in placeholders from the bottom up. 
        A needs to be the result of increasing 3 (the value to its left) by 0 (the value below it); 
        this means A must be 3:

                0   3   6   9  12  15   B
                3   3   3   3   3   3
                    0   0   0   0   0
        Finally, you can fill in B, which needs to be the result of increasing 15 (the value to its left) 
        by 3 (the value below it), or 18:

                0   3   6   9  12  15  18
                3   3   3   3   3   3
                    0   0   0   0   0
        So, the next value of the first history is 18.

        Finding all-zero differences for the second history requires an additional sequence:

                1   3   6  10  15  21
                2   3   4   5   6
                    1   1   1   1
                    0   0   0
        Then, following the same process as before, work out the next value in each sequence from the bottom up:

                1   3   6  10  15  21  28
                2   3   4   5   6   7
                    1   1   1   1   1
                    0   0   0   0
        So, the next value of the second history is 28.

        The third history requires even more sequences, but its next value can be found the same way:

                10  13  16  21  30  45  68
                3   3   5   9  15  23
                    0   2   4   6   8
                    2   2   2   2
                        0   0   0
        So, the next value of the third history is 68.

        If you find the next value for each history in this example and add them together, you get 114.

        Analyze your OASIS report and extrapolate the next value for each history. 
        What is the sum of these extrapolated values?
    Part 2:
        Of course, it would be nice to have even more history included in your report.
        Surely it's safe to just extrapolate backwards as well, right?

        For each history, repeat the process of finding differences until the sequence of differences is entirely zero.
        Then, rather than adding a zero to the end and filling in the next values of each previous sequence, 
        you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

        In particular, here is what the third example history looks like when extrapolating back in time:

                5  10  13  16  21  30  45
                5   3   3   5   9  15
                -2   0   2   4   6
                    2   2   2   2
                        0   0   0
        Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

        Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history.
        Adding all three new values together produces 2.

        Analyze your OASIS report again, this time extrapolating the previous value for each history.
        What is the sum of these extrapolated values?
"""
def print_history(list):
    space = 0
    for r in list:
        for o in range(space):
            print(" ", end="")
        for i in r:
            print(i,end="  ")
        space+=2
        print()


def rec_n(list1, list2):
    list3 = []
    n = 0
    n = int(list1[0]) - int(list2[0])
    list3.append(str(n))
    for i in list1:
        list3.append(i)
    return list3

def parse(filename):
    listat = []
    for i in open(filename):
        lista = []
        for n in i.strip().split(" "):
            lista.append(n)
        listat.append(lista)
    return listat

def Part1(filename):
    tot = 0
    listat = parse(filename)
    print(listat)
    print("HISTORY:")
    for l in listat:
        history = []
        history.append(l)
        while True:
            listan=[]
            exit = True
            n = 0
            #print("PASS", history[-1])

            for i in history[-1]:
                #print(i, end=" ")
                if int(i) != 0:
                    #print("False")
                    exit = False
            if exit:
                break

            while n < len(history[-1])-1:
                listan.append(int(history[-1][n+1])-int(history[-1][n]))
                n+=1
            history.append(listan)

        print_history(history)
        print("--------------")
        print("RECOVERY NUMBER: ", end="")
        for i in range(len(history)-1, 0, -1):
            history[i-1] = rec_n(history[i], history[i-1])
        print(history[0][-1])
        tot += int(history[0][-1])
    print("TOTAL: ", tot)

def Part2(filename):
    tot = 0
    listat = parse(filename)
    print(listat)
    print("HISTORY:")
    for l in listat:
        history = []
        history.append(l)
        while True:
            listan=[]
            exit = True
            n = 0
            #print("PASS", history[-1])

            for i in history[-1]:
                #print(i, end=" ")
                if int(i) != 0:
                    #print("False")
                    exit = False
            if exit:
                break

            while n < len(history[-1])-1:
                listan.append(int(history[-1][n+1])-int(history[-1][n]))
                n+=1
            history.append(listan)
        print_history(history)

        print("--------------")
        print("RECOVERY NUMBER: ", end="")
        for i in range(len(history)-1, 0, -1):
            history[i-1] = rec_n(history[i-1], history[i])
        print(history[0][0])
        print_history(history)
        print("--------------")
        tot += int(history[0][0])
    print("TOTAL: ", tot)


if __name__ == "__main__":
    #Part1("Advent9/input.txt")
    Part2("Advent9/input.txt")