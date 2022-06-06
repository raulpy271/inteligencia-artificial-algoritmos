
from src.graph import Graph

def get_next_node(visited_nodes, nodes):
    for node_name, weight in nodes:
        if not node_name in visited_nodes:
            return (node_name, weight)
    return None

def busca_em_profundidade(graph: Graph, origin, target):
    path = [(origin, 0)]
    visited_nodes = [origin]
    while True:
        adjacents = graph.get_relations_of(path[-1][0])
        next_node = get_next_node(visited_nodes, adjacents)
        if next_node:
            path.append(next_node)
            visited_nodes.append(next_node[0])
            if next_node[0] == target:
                break
            else:
                continue
        else:
            if len(path) < 2:
                return []
            else:
                path.pop()
    return path
