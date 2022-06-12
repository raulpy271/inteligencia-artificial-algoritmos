
from busca_em_profundidade.src.graph import Graph
from busca_A_estrela.distancias import Distancias

def obtem_valor_heuristico(no_atual, proximo_no, destino, graph: Graph, distancias: Distancias):
    return distancias.obtem_distancia(proximo_no, destino) + graph.get_weight(no_atual, proximo_no)
