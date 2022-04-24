

visited = []

q = []

def evalPos(board, newpos, visited):
    #check:
    #out of bounds
    l = len(board)
    if newpos[0] < 0 or newpos[0] > l or newpos[1] < 0 or newpos[1] > l:
        return False
    #collide with piece
    if board[newpos[0]][newpos[1]] != ' ' : 
        return False
    #adjacent/visited position
    for i in range(len(visited)):
        v = visited[i] 
        if (v[0],v[1]) == newpos or (v[0]+1,v[1]) == newpos or (v[0]-1,v[1]) == newpos or (v[0],v[1]+1) == newpos or (v[0],v[1]-1) == newpos: 
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

        if currpos == (0,len(board)-1) : 
            return currpath

        visited.append(currpos)
        neighbors = [(currpos[0]-1,currpos[1]),(currpos[0]+1,currpos[1]),(currpos[0],currpos[1]-1),(currpos[0],currpos[1]+1)]
        for i in range(4):
            nb = neighbors[i]

            if evalPos(board, nb, currpath) & nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)


board = [[],[],[],[]]
print(bfs(board,(board[-1][0]),[]))

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

            if evalPos(board, nb, currpath) & nb not in visited:
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

            if evalPos(board, nb, currpath) & nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)
                depth-=1


#def uniform_cost()

#def greedy()

#def astar()