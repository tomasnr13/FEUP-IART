from queue import PriorityQueue
import time
from webbrowser import get


def getPath(node):

    path = [node]
    currNode = node

    while (True):
        currNode = currNode.previousNode
        if (not currNode): break
        path.append(currNode)

    path.reverse()

    return path

#breadth first search
def bfs(initial, cond):
    start_time = time.time()

    nodesToVisit = [initial]
    visited = []

    while (nodesToVisit):
        currNode = nodesToVisit.pop(0)

        if (currNode in visited): 
             continue

        visited.append(currNode)

        if (cond(currNode)):
            # return f'BFS Result: \n{getPath(currNode)}\nVisited {len(visited) + 1}\nTime: {round(time.time() - start_time, 6)} seconds\n'
            return getPath(currNode)

        edgeNodes = currNode.edgeNodes()
        nodesToVisit += edgeNodes

    return None

#depth first search
def dfs(node, cond, visited=[]):
    start_time = time.time()

    if (not node or node in visited):
        return None
    if (cond(node)):
        # return f'DFS Result: \n{getPath(node)}\nVisited {len(visited) + 1} nodes:\n{visited + [node]}\nTime: {round(time.time() - start_time, 6)} seconds\n'
        return getPath(node)

    for edgeNode in node.edgeNodes():
        if (edgeNode in visited): continue
        val = dfs(edgeNode, cond, visited + [node])
        if (val): return val

    return None


#depth first search
def dls(node, cond, maxDepth, visited=[], depth=0):
    start_time = time.time()

    if (node in visited): return (None, False)
    if (cond(node)):
        # return (f'DLS Result (max depth of {maxDepth}):\n{getPath(node)}\n Visited {len(visited) + 1} nodes:\n{visited + [node]}\nTime: {round(time.time() - start_time, 6)} seconds\n', False)
        return (getPath(node), False)
            
    if (maxDepth == depth): return (None, visited != [])

    for edgeNode in node.edgeNodes():
        if (edgeNode in visited): continue
        finalNode, _ = dls(edgeNode, cond, maxDepth, visited + [node],
                           depth + 1)
        if (finalNode): return (finalNode, False)

    return (None, visited == [])

#iterative deepening 
def it_deep(initial, cond):

    path = None
    curDepth = 1

    while (True):

        path, remaining = dls(initial, cond, curDepth)
        if (path): return path
        if (not remaining): return None

        curDepth += 1

#uniform cost
def ucost(initial, cond):
    start_time = time.time()

    nodesToVisit = PriorityQueue()
    nodesToVisit.put((initial.distance, initial))
    visited = []

    while (not nodesToVisit.empty()):
        aux, currNode = nodesToVisit.get()

        if (currNode in visited): continue

        visited.append(currNode)

        if (cond(currNode)):
            # return f'UCost Result: {getPath(currNode)}\n Visited Nodes: {len(visited) + 1} \nTime: {round(time.time() - start_time, 6)} seconds\n'
            return getPath(currNode)

        edgeNodes = currNode.edgeNodes(currNode.distance + 1)

        for node in edgeNodes:
            nodesToVisit.put((node.distance, node))

    return None


def greedy(initial, cond, heuristic, board):
    start_time = time.time()

    nodesToVisit = PriorityQueue()
    nodesToVisit.put((heuristic(initial, board), initial))

    visited = []

    while (not nodesToVisit.empty()):
        aux, currNode = nodesToVisit.get()

        if (currNode in visited): continue

        visited.append(currNode)

        if (cond(currNode)):
            # return f'Greedy Result: Visited Nodes: {len(visited)}, {getPath(currNode)} \nTime: {round(time.time() - start_time, 6)} seconds\n'
            return getPath(currNode)

        edgeNodes = currNode.edgeNodes()

        for node in edgeNodes:
            nodesToVisit.put((heuristic(node, board), node))

    return None


def astar(initial, cond, heuristic, board):
    start_time = time.time()
    
    nodesToVisit = PriorityQueue()
    nodesToVisit.put((heuristic(initial, board), initial))
    visited = []

    while (not nodesToVisit.empty()):
        aux, currNode = nodesToVisit.get()

        if (currNode in visited): continue

        visited.append(currNode)

        if (cond(currNode)):
            # return f'AStar Result: Visited Nodes: {len(visited) + 1} , {getPath(currNode)} \nTime: {round(time.time() - start_time, 6)} seconds\n'
            return getPath(currNode)

        edgeNodes = currNode.edgeNodes(currNode.distance + 1)

        for node in edgeNodes:
            heuristicNode = node.distance + heuristic(node, board)
            nodesToVisit.put((heuristicNode, node))

    return None
