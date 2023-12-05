"""
ADVENT OF CODE 2023 - DAY 5
Author: Michael Tezza
Date: 05/12/2023
Description: 
    Part 1: 
        The gardener and his team want to get started as soon as possible, so they'd like to know 
        the closest location that needs a seed. Using these maps, 
        find the lowest location number that corresponds to any of the initial seeds. 
        To do this, you'll need to convert each seed number through other categories until you can 
        find its corresponding location number. 
        In this example, the corresponding types are:

            Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
            Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
            Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
            Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
            So, the lowest location number in this example is 35.

        What is the lowest location number that corresponds to any of the initial seed numbers?
    Part 2:
        Everyone will starve if you only plant such a small number of seeds. 
        Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

        The values on the initial seeds: line come in pairs. 
        Within each pair, the first value is the start of the range and the second value is the length 
        of the range. So, in the first line of the example above:

        seeds: 79 14 55 13
        This line describes two ranges of seed numbers to be planted in the garden. 
        The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. 
        The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

        Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

        In the above example, the lowest location number can be obtained from seed number 82, 
        which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, 
        and location 46. So, the lowest location number is 46.

        Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. 
        What is the lowest location number that corresponds to any of the initial seed numbers?
"""
def parse(filename):
    seed = []
    soil = []
    fertilizer = []
    water = []
    light = []
    temperature = []
    humidity = []
    location = []
    n = 0 # 0 = seed, 1 = soil, 2 = fertilizer, 3 = water, 4 = light, 5 = temperature, 6 = humidity, 7 = location 
    firstRow = True
    for row in open(filename):
        if firstRow:
            firstRow = False
            row = row.strip()
            seed = row.split(":")[1].split(" ")[1:]
            print(seed)
        else:
            if row == "\n":
                pass
            elif row[0].isalpha():
                if row.split(":")[0] == "seed-to-soil map":
                    print("seed-to-soil map:")
                    n = 1
                elif row.split(":")[0] == "soil-to-fertilizer map":
                    print("soil-to-fertilizer map:")
                    n = 2
                elif row.split(":")[0] == "fertilizer-to-water map":
                    print("fertilizer-to-water map:")
                    n = 3
                elif row.split(":")[0] == "water-to-light map":
                    print("water-to-light map:")
                    n = 4
                elif row.split(":")[0] == "light-to-temperature map":
                    print("light-to-temperature map:")
                    n = 5
                elif row.split(":")[0] == "temperature-to-humidity map":
                    print("temperature-to-humidity map:")
                    n = 6
                elif row.split(":")[0] == "humidity-to-location map":
                    print("humidity-to-location map:")
                    n = 7
            else:
                if n == 1:
                    row = row.strip()
                    row = row.split(" ")
                    soil.append(row)
                elif n == 2:
                    row = row.strip()
                    row = row.split(" ")
                    fertilizer.append(row)
                elif n == 3:
                    row = row.strip()
                    row = row.split(" ")
                    water.append(row)
                elif n == 4:
                    row = row.strip()
                    row = row.split(" ")
                    light.append(row)
                elif n == 5:
                    row = row.strip()
                    row = row.split(" ")
                    temperature.append(row)
                elif n == 6:
                    row = row.strip()
                    row = row.split(" ")
                    humidity.append(row)
                elif n == 7:
                    row = row.strip()
                    row = row.split(" ")
                    location.append(row)
    return seed, soil, fertilizer, water, light, temperature, humidity, location  

def DownUp(n, lista):
    for i in lista:
        if n >= int(i[1]) and n <= int(i[1])+int(i[2]):
            return int(i[0])+ (n-int(i[1]))
    return n

def UpDown(n, lista):
    for i in lista:
        if n >= int(i[0]) and n <= int(i[0])+int(i[2]):
            return int(i[1])+ (n-int(i[0]))
    return n

#Part 1  
def Part1(filename):
    seed, soil, fertilizer, water, light, temperature, humidity, location = parse(filename)
    lista = []
    for i in seed:
        n = DownUp(int(i), soil)
        n = DownUp(n, fertilizer)
        n = DownUp(n, water)
        n = DownUp(n, light)
        n = DownUp(n, temperature)
        n = DownUp(n, humidity)
        n = DownUp(n, location)
        lista.append(n)
    print(min(lista))
    
#Part 2
def Part2(filename):
    seed, soil, fertilizer, water, light, temperature, humidity, location = parse(filename)
    lista = []
    listag = []
    i = 0
    s1,s2,s3,s4,s5,s6,s7,s8 = 0,0,0,0,0,0,0,0
    while i < len(seed)-1:
        print(i)
        s1 = DownUp(int(seed[i]), soil)
        s2 = DownUp(s1, fertilizer)
        s3 = DownUp(s2, water)
        s4 = DownUp(s3, light)
        s5 = DownUp(s4, temperature)
        s6 = DownUp(s5, humidity)
        s7 = DownUp(s6, location)
        lista.append(s7)
        listag = minimo([[0,s7]], location)
        listag = minimo(listag, humidity)
        listag = minimo(listag, temperature)
        listag = minimo(listag, light)
        listag = minimo(listag, water)
        listag = minimo(listag, fertilizer)
        listag = minimo(listag, soil)

        for a in range(int(seed[i])+1, int(seed[i])+ int(seed[i+1])):
            for g in listag:
                if a >= g[0] and a <= g[1]:
                    s1 = DownUp(int(a), soil)
                    s2 = DownUp(s1, fertilizer)
                    s3 = DownUp(s2, water)
                    s4 = DownUp(s3, light)
                    s5 = DownUp(s4, temperature)
                    s6 = DownUp(s5, humidity)
                    s7 = DownUp(s6, location)
                    lista.append(s7)
                    listag = minimo([[0,s7]], location)
                    listag = minimo(listag, humidity)
                    listag = minimo(listag, temperature)
                    listag = minimo(listag, light)
                    listag = minimo(listag, water)
                    listag = minimo(listag, fertilizer)
                    listag = minimo(listag, soil)
                    break
                

        i +=2
    print(min(lista))

def minimo(lista1, lista2):
    n_lista = []
    for i in lista2:
        for a in lista1:
            if a[0] <= int(i[0]):
                min = a[1]
            else:
                min = int(i[0])
            if a[1] >= int(i[0])+int(i[2]):
                max = a[1]
            else:
                max = int(i[1])
            n_lista.append([min,max])
    return n_lista
            

            
    return n_lista
if __name__ == "__main__":
    #Part1("./Advent5/input.txt")#261668924
    Part2("./Advent5/input.txt")#24261545
