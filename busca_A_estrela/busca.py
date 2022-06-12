
from busca_A_estrela.heuristica import obtem_valor_heuristico
from busca_em_profundidade.src.graph import Graph

def obtem_proximo_no_usando_heuristica(no_atual, nodes, target, graph, distancias):
    mais_proximo_usando_heuristica = nodes[0]
    valor_heuristico_do_mais_proximo = obtem_valor_heuristico(no_atual, nodes[0][0], target, graph, distancias)
    for adjacent_name, adjacent_weight in nodes:
        heuristica = obtem_valor_heuristico(no_atual, adjacent_name, target, graph, distancias)
        if heuristica < valor_heuristico_do_mais_proximo:
            valor_heuristico_do_mais_proximo = heuristica
            mais_proximo_usando_heuristica = adjacent_name, adjacent_weight
    return mais_proximo_usando_heuristica

def busca_a_estrela(graph: Graph, origin, target, distancias):
    path = [(origin, 0)]
    while True:
        adjacents = graph.get_relations_of(path[-1][0])
        if adjacents:
            next_node = obtem_proximo_no_usando_heuristica(path[-1][0], adjacents, target, graph, distancias)
        else:
            next_node = None
        if next_node:
            path.append(next_node)
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
