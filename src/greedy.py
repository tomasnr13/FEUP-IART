class Node:
    """
    attributes:
        - value (str) -> value of the node NÃO SEI QUAL É O VALOR DO NODE
        - x (int) -> x-coordinate of the node
        - y (int) -> y-coordinate of the node
        - heuristic_value (int) -> represents the diference between the number of each piece possible capture options
        - neighbors (list) -> list with the nodes the current node is connected
        - parent (Node) -> the parent node of the current node
    """

    def __init__(self, value, coordinates, neighbors=[]):
        self.value = value
        self.x = coordinates[1]
        self.y = coordinates[0]
        self.heuristic_value = -1
        self.neighbors = neighbors
        self.parent = None
    
    def __gt__(self, other):
        """
        defines wich node, between the current and other one, has the greater value
        starts comparing the heuristic value and if both nodes have the same value, NÃO SEI O QUE FAZER NESTE CASO, para já ta a comparar o valor
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
        
    class Greedy:
        """
        attributes:
            - graph (Graph) -> 
            - 
        """