
class Distancias:
    def __init__(self):
        self.distancias = {
        }
    
    def add_distancias(self, ponto_inicial, ponto_final, distancia):
        self.distancias[f'{ponto_inicial}.{ponto_final}'] = distancia

    def obtem_distancia(self, ponto_inicial, ponto_final):
        key = f'{ponto_inicial}.{ponto_final}' 
        if key in self.distancias:
            return self.distancias[key]
        else:
            raise Exception('Distancia não encontrada!')


