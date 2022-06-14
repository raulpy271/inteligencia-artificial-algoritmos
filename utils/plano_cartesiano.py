import math

class PlanoCartesiano:
    def __init__(self):
        self.pontos = {
        }
    
    def add_pontos(self, ponto_nome, x, y):
        self.pontos[ponto_nome] = (x, y)

    def obtem_distancia(self, ponto_inicial, ponto_final):
        if ponto_inicial in self.pontos and ponto_final in self.pontos:
            x_i, y_i = self.pontos[ponto_inicial]
            x_f, y_f = self.pontos[ponto_final]
            return math.sqrt(
                ((x_f - x_i) ** 2) + ((y_f - y_i) ** 2)
            )
        else:
            raise Exception('Ponto buscado não está no plano cartesiano')


