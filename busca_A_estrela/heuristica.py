
from utils.plano_cartesiano import PlanoCartesiano

def obtem_valor_heuristico(no_atual, proximo_no, destino, plano: PlanoCartesiano):
    return plano.obtem_distancia(proximo_no, destino) + plano.obtem_distancia(no_atual, proximo_no)
