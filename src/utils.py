def getDistance(position,board):
    return position[0] + len(board)-position[1]

def validPos(board, newpos, visited):
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
    adjs = [(newpos[0]-1,newpos[1]), (newpos[0]+1,newpos[1]), (newpos[0],newpos[1]-1), (newpos[0],newpos[1]+1)]
    visited_adjs = [pos for pos in adjs if pos in visited]

    if len(visited_adjs) > 1:
        return False

    return True