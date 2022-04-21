import main

visited = []
q = []

def bfs(board, position, visited):
    q.append([position])
    while q:
        currpath = q.pop(0)
        currpos = currpath[-1]

        if currpos == board[0][-1] : 
            return currpath

        visited.append(currpos)
        neighbors = [(currpos[0]-1,currpos[1]),(currpos[0]+1,currpos[1]),(currpos[0],currpos[1]-1),(currpos[0],currpos[1]+1)]
        for i in range(4):
            nb = neighbors[i]

            if main.evalPos(board, nb, currpath) & nb not in visited:
                newpath = list(currpath)
                newpath.append(nb)
                q.append(newpath)


board = main.defaultBoard()
print(bfs(board,(board[-1][0]),[]))

#def dfs(board, initpos):

#def iter_deep():

#def uniform_cost()

#def greedy()

#def astar()