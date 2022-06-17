
from utils.graph import Graph
from busca_em_profundidade.busca import busca_em_profundidade

def executa_busca_exemplo():
    cities = Graph()
    cities.insert(node='arad', adjacent_to='timisoara', weight=118)
    cities.insert(node='arad', adjacent_to='sibiu', weight=140)
    cities.insert(node='arad', adjacent_to='zerind', weight=75)
    cities.insert(node='zerind', adjacent_to='oradea', weight=71)
    cities.insert(node='oradea', adjacent_to='sibiu', weight=151)
    cities.insert(node='timisoara', adjacent_to='lugoj', weight=111)
    cities.insert(node='lugoj', adjacent_to='mehadia', weight=70)
    cities.insert(node='mehadia', adjacent_to='brobeta', weight=75)
    cities.insert(node='brobeta', adjacent_to='craiova', weight=120)
    cities.insert(node='craiova', adjacent_to='rimmicu', weight=146)
    cities.insert(node='rimmicu', adjacent_to='sibiu', weight=80)
    cities.insert(node='sibiu', adjacent_to='fagaras', weight=99)
    cities.insert(node='fagaras', adjacent_to='bucarest', weight=210)
    cities.insert(node='rimmicu', adjacent_to='pitesti', weight=97)
    cities.insert(node='craiova', adjacent_to='pitesti', weight=138)
    cities.insert(node='pitesti', adjacent_to='bucarest', weight=101)

    return busca_em_profundidade(cities, 'arad', 'bucarest')

if __name__ == '__main__':

    print(
        executa_busca_exemplo()
    )
