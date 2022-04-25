import chess, utils, main, math

visited = []

q = []

def algorithmCall(alg, board, position, visited):
    visited = []
    q = []
    if(alg == "bfs"):
        bfs(board, position, visited)
    elif(alg == "dfs"):
        dfs(board, position, visited)
    elif(alg == "id"):
        iter_deep(board, position, visited)
    # elif(alg == "uc"):
        # uniform_cost(board, position, visited)
    # elif(alg == "g"):
        # greedy(board, position, visited)
    # elif(alg == "as"):
        # astar(board, position, visited)
    else:
        print("wrong algorithm name!")


def getDistance(position, board):
    return position[0] + len(board) - 1

def eval_function(position, currpath, board):
    # getcaps(lastpos)
    # getcaps(newpos)
    # getdistance(newpos)
    boardd = board[:]
    newboard = board[:]
    for line in range(len(board)):
        for col in range(len(board)):
            if (line, col) in currpath:
                boardd[line][col] = 1
                newboard[line][col] = 1

    newboard[position[0]][position[1]] = 1

    nb_count = -1
    b_count  = -1
    d = getDistance(position, board)
    for line in range(len(boardd)):
        for col in range(len(newboard)):
            if isinstance(boardd[line][col], chess.ChessPiece):
                b_count = len(
                    board[line][col].currentCaptures(boardd, line, col))
            if isinstance(newboard[line][col], chess.ChessPiece):
                nb_count = len(
                    board[line][col].currentCaptures(newboard, line, col))

    return (nb_count-b_count)+d/4

# def uniform_cost()


def bfs(board, position, visited):
    
    q.append([position])

    while q:
        currpath = q.pop(0)
        currpos = currpath[-1]
        print('currpath: ',currpath)
        print('currpos: ',currpos)

        if currpos == (0,len(board)-1) : 
            return currpath

        visited.append(currpos)
        neighbors = [(currpos[0]-1,currpos[1]),(currpos[0]+1,currpos[1]),(currpos[0],currpos[1]-1),(currpos[0],currpos[1]+1)]
        heuristic_value = math.inf
        
        for i in range(4):
            nb = neighbors[i]

            if utils.validPos(board, nb, currpath) and nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                print('newpath: ',newpath)
                q.append(newpath)

def dfs(board, currpos, visited):
    q.append([currpos])

    while q:
        currpath = q.pop()
        currpos = currpath[-1]

        if currpos == (0,len(board)-1): 
            return currpath

        visited.append(currpos)
        neighbors = [(currpos[0],currpos[1]+1),(currpos[0],currpos[1]-1),(currpos[0]+1,currpos[1]),(currpos[0]-1,currpos[1])]
        for i in range(4):
            nb = neighbors[i]

            if utils.validPos(board, nb, currpath) and nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)
            

def id_dfs_aux(board,currpos,depth):
    q.append([currpos])

    while q:
        currpath = q.pop()
        currpos = currpath[-1]

        if currpos == (0,len(board)-1) : 
            return currpath

        if depth == 0 : 
            return []

        visited.append(currpos)
        neighbors = [(currpos[0],currpos[1]+1),(currpos[0],currpos[1]-1),(currpos[0]+1,currpos[1]),(currpos[0]-1,currpos[1])]
        for i in range(4):
            nb = neighbors[i]

            if utils.validPos(board, nb, currpath) and nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)
                depth-=1

def iter_deep(board, currpos, visited, maxdepth):
    for i in range(maxdepth):
        visited = []
        retpath = id_dfs_aux(board,currpos,visited, i)
        if retpath != []:
            return retpath
    return retpath


def evalFunction(position, currpath, board):
    #getcaps(lastpos)
    #getcaps(newpos)
    #getdistance(newpos)
    boardd = board[:]
    newboard = board[:]
    for line in range(len(board)):
        for col in range(len(board)):
            if (line,col) in currpath:
                boardd[line][col] = 1
                newboard[line][col] = 1

    newboard[position[0]][position[1]]=1

    d = utils.getDistance(position, board)

    for line in range(len(board)):
        for col in range(len(board)):
            if isinstance(boardd[line][col], chess.ChessPiece):
                b_count = len(board[line][col].currentCaptures(boardd, line, col))
            if isinstance(newboard[line][col], chess.ChessPiece):
                nb_count = len(board[line][col].currentCaptures(newboard, line, col))

    return (nb_count-b_count)+d/4
    
#def uniform_cost()

#def greedy()

#def astar()

board = main.defaultBoard()
print(bfs(board,(4,0),[]))
