import math

class Node:
    """
    this class is used to represent each vertex in the graph
    atributes: 
       - value (str) -> represents the value of the node (NÃO SEI O QUE É)
       - heuristic_value (int) -> represents the diference between the number of each piece possible capture options
       - neighbors (list) -> list with the nodes the cur node is connected
       - parent (node) -> parent node of the cur node
    """

    def __init__(self, value, neighbors=[]):
        self.value = value
        self.heuristic_value = math.inf
        self.neighbors = neighbors

    def __gt__(self, other):
        """
        chooses the node with greater value (between cur node and other one)
        compares the heuristic value and then NÃO SEI O QUE COMPARAR THEN, PARA JÁ TA O VALOR
        parameters:
           - other (Node) -> represents the other node with which the cur node is compared
        result:
            boolean
        """
        if isinstance(other, Node):
            if self.heuristic_value > other.heuristic_value:
                return True
            if self.heuristic_value < other.heuristic_value:
                return False
            return self.value > other.value


class UCS:
    def __init__(self, graph, start_pos, target):
        self.graph = graph
        self.start = graph.find_node(start_pos)
        self.target = graph.find_node(target)
        self.opened = []
        self.closed = []

    def calculateCaptures(self, parent, child):
        """
        calculate and return the number of captures for each chess piece, from the start to the child node
        if the heuristic valus has already been calculated and is smaller than the new value, the method returns the old value, otherwise returns the new value and note the parent as the parent node of the child
        parameters:
           - parent (node) -> the parent node
           - child (node) -> the child node
        result:
            int
        """
        for neighbor in parent.neighbors:
            if neighbor[0] == child:
                num_captures = parent.heuristic_value + neighbor[1]
                if num_captures > child.heuristic_value:
                    pass
