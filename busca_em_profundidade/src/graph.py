
class Graph:

    NO_RELATION = "NO_RELATION"

    def __init__(self):
        self.edges = []

    def insert(self, node, adjacent_to, weight):
        self.edges.append((node, adjacent_to, weight))
    
    def get_relations_of(self, node):
        children = []
        for node_i, adjacent_to_i, weight in self.edges:
            if node_i == node:
                children.append((adjacent_to_i, weight))
            elif adjacent_to_i == node:
                children.append((node_i, weight))
        return children

    def get_weight(self, node, adjacent_node):
        for node_i, adjacent_to_i, weight in self.edges:
            if node_i == node and adjacent_to_i == adjacent_node:
                return weight
            elif adjacent_to_i == node and node_i ==  adjacent_node:
                return weight
        return Graph.NO_RELATION

