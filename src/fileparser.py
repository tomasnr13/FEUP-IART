
def fileParser(filename):
    f = open("src/files/" + filename, "r")

    board = []
    size = int(f.readline())
    
    for _ in range(size):
        line = f.readline()
        line = line.split()
        for x in range(size):
            if line[x] == '0':
                line[x] = 0
        board += [line]
    
    return board


print(fileParser("level1.txt"))
