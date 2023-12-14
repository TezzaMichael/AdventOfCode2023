def parse(string):
    lista = []
    for i in string.split(" ")[0]:
        lista.append(i)
    numbers = []
    for i in string.split(" ")[1].split(","):
        numbers.append(int(i))
    return lista, numbers

def count_resolution(lista, numbers):
    pass

def Part1(filename):
    n = 0
    for i in open(filename):
        lista, numbers = parse(i.strip())
        print(lista, numbers)
        n+= count_resolution(lista, numbers)
    print(n)
    return n

if __name__ == "__main__":
    Part1("Advent12/input.txt")