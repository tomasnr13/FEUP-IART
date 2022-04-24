

visited = []

q = []

def evalPos(board, newpos, visited):
    #check:
    #out of bounds
    l = len(board)
    if newpos[0] < 0 or newpos[0] >= l or newpos[1] < 0 or newpos[1] >= l:
        return False
    #collide with piece
    if board[newpos[0]][newpos[1]] != 0 : 
        return False
    #visited position  
    if newpos in visited :
        return False
    #adjacent position 
    adjs=0
    if (newpos[0]-1,newpos[1]) in visited : 
        adjs+=1
    if (newpos[0]+1,newpos[1]) in visited : 
        adjs+=1
    if (newpos[0],newpos[1]-1) in visited : 
        adjs+=1
    if (newpos[0],newpos[1]+1) in visited : 
        adjs+=1
    if adjs>1:
        return False

    return True



def algorithmcall(alg, board, position, visited):
    visited = []
    q = []
    if(alg == "bfs"):
        bfs(board, position, visited)
    elif(alg == "dfs"):
        dfs(board, position, visited)
    elif(alg == "id"):
        iter_deep(board, position, visited)
    #elif(alg == "uc"):
        #uniform_cost(board, position, visited)
    #elif(alg == "g"):
        #greedy(board, position, visited)
    #elif(alg == "as"):
        #astar(board, position, visited)
    else:
        print("wrong algorithm name!")
    

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
        for i in range(4):
            nb = neighbors[i]

            if evalPos(board, nb, currpath) and nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                print('newpath: ',newpath)
                q.append(newpath)

def dfs(board, currpos, visited):
    q.append([currpos])

    while q:
        currpath = q.pop()
        currpos = currpath[-1]

        if currpos == (0,len(board)-1) : 
            return currpath

        visited.append(currpos)
        neighbors = [(currpos[0],currpos[1]+1),(currpos[0],currpos[1]-1),(currpos[0]+1,currpos[1]),(currpos[0]-1,currpos[1])]
        for i in range(4):
            nb = neighbors[i]

            if evalPos1(board, nb, currpath) and nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)


def iter_deep(board, currpos, visited, maxdepth):
    for i in range(maxdepth):
        visited = []
        retpath = id_dfs_aux(board,currpos,visited, i)
        if retpath != []:
            return retpath
    return retpath
            

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

            if evalPos(board, nb, currpath) and nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)
                depth-=1


#def uniform_cost()

#def greedy()

#def astar()

board = [[0, 0, 0, 0, 0],
        [0, 'T', 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 'K', 0, 0, 0],
        [0, 0, 0, 0, 0]]
print(dfs(board,(4,0),[]))