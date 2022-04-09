
def fileParser(filename):
    f = open(filename, "r")

    board = []
    size = int(f.readline())
    
    for _ in range(size):
        line = f.readline()
        line = line.split()
        for x in range(size):
            if line[x] == '0' or line[x] == '1':
                line[x] = int(line[x])
        board += [line]
    
    return board


print(fileParser("resources/level1.txt"))
