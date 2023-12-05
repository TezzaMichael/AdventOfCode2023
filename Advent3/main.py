"""
ADVENT OF CODE 2023 - DAY 3
Author: Michael Tezza
Date: 03/12/2023
Description: 
    Part 1: 
        The engine schematic (your puzzle input) consists of a visual representation of the engine. 
        There are lots of numbers and symbols you don't really understand, but apparently any number 
        adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
        (Periods (.) do not count as a symbol.)

        Here is an example engine schematic:

                    467..114..
                    ...*......
                    ..35..633.
                    ......#...
                    617*......
                    .....+.58.
                    ..592.....
                    ......755.
                    ...$.*....
                    .664.598..
        In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
        114 (top right) and 58 (middle right). 
        Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

        Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers 
        in the engine schematic?

    Part 2:
        The missing part wasn't the only issue - one of the gears in the engine is wrong.
        A gear is any * symbol that is adjacent to exactly two part numbers. 
        Its gear ratio is the result of multiplying those two numbers together.

        This time, you need to find the gear ratio of every gear and add them all up so that the engineer 
        can figure out which gear needs to be replaced.

        Consider the same engine schematic again:

                        467..114..
                        ...*......
                        ..35..633.
                        ......#...
                        617*......
                        .....+.58.
                        ..592.....
                        ......755.
                        ...$.*....
                        .664.598..
        In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35,
        so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490.
        (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) 
        Adding up all of the gear ratios produces 467835.

        What is the sum of all of the gear ratios in your engine schematic?
"""
def parse(filename):
    digit_dict = {}
    symbol_dict = {}

    with open(filename, "r") as f:
        for y, line in enumerate(map(str.strip, f.readlines())):
            for x, char in enumerate(line):
                if char.isdigit():
                    digit_dict[(x, y)] = int(char)
                elif char.isalpha():
                    symbol_dict[(x, y)] = char

    return digit_dict, symbol_dict

# Funzioni di supporto
def trova_vicini(nodo):
    x, y = nodo
    return [(x+dx, y+dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0]

def completa_numero(nodo, digit_dict):
    x, y = nodo
    num_string = str(digit_dict[nodo])
    num_coords = [nodo]

    for dx, dy in [(1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        while (nx, ny) in digit_dict:
            num_string = str(digit_dict[(nx, ny)]) + num_string if dx == -1 else num_string + str(digit_dict[(nx, ny)])
            num_coords.append((nx, ny))
            nx, ny = nx + dx, ny + dy

    return num_string, num_coords

def trova_numeri_vicini(vicini, digit_dict):
    numeri_vicini = []

    for nodo in vicini:
        if nodo in digit_dict:
            numero, coord_visitati = completa_numero(nodo, digit_dict)
            if coord_visitati not in numeri_vicini:
                numeri_vicini.append(coord_visitati)

    return [sum(digit_dict[coord] for coord in coords) for coords in numeri_vicini]

# Funzioni principali
def Part1(input_puzzle):
    digit_dict, symbol_dict = input_puzzle
    tot = sum(trova_numeri_vicini(trova_vicini(coords), digit_dict) for coords in symbol_dict.keys())
    print(tot)

def Part2(input_puzzle):
    digit_dict, symbol_dict = input_puzzle
    tot = sum(adj[0] * adj[1] for coords, adj in ((coords, trova_numeri_vicini(trova_vicini(coords), digit_dict)) for coords in symbol_dict if len(trova_numeri_vicini(trova_vicini(coords), digit_dict)) == 2))
    print("Soluzione Parte 2:", tot)
    print(tot)

if __name__ == "__main__":
    input_puzzle = parse("./Advent3/input.txt")
    Part1(input_puzzle)
    Part2(input_puzzle)