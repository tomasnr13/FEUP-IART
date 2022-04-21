from curses.ascii import isdigit
import chess

def fileParser(filename):
    f = open(filename, "r")

    board = []
    size = int(f.readline())
    
    for _ in range(size):
        line = f.readline()
        line = line.split()
        for x in range(size):
            elem = line[x]
            if isdigit(elem):
                line[x] = int(elem)
            else:
                if elem == 'T':
                    line[x] = chess.Tower()
                elif elem == 'H':
                    line[x] = chess.Horse()
                elif elem == 'B':
                    line[x] = chess.Bishop()
                elif elem == 'Q':
                    line[x] = chess.Queen()
                else:
                    line[x] = chess.King()
        board += [line]
    
    return board


#print(fileParser("resources/level1.txt"))
