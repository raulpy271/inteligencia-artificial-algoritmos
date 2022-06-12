
from busca_A_estrela.distancias import Distancias
from busca_A_estrela.busca import busca_a_estrela
from busca_em_profundidade.src.graph import Graph

if __name__ == '__main__':
    cities = Graph()
    distancias = Distancias()
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

    distancias.add_distancias('arad', 'bucarest', 366)
    distancias.add_distancias('bucarest', 'bucarest', 0)
    distancias.add_distancias('craiova', 'bucarest', 160)
    distancias.add_distancias('brobeta', 'bucarest', 242)
    distancias.add_distancias('eforie', 'bucarest', 161)
    distancias.add_distancias('fagaras', 'bucarest', 176)
    distancias.add_distancias('giurgiu', 'bucarest', 77)
    distancias.add_distancias('hirsova', 'bucarest', 151)
    distancias.add_distancias('lasi', 'bucarest', 226)
    distancias.add_distancias('lugoj', 'bucarest', 244)
    distancias.add_distancias('mehadia', 'bucarest', 241)
    distancias.add_distancias('neamt', 'bucarest', 234)
    distancias.add_distancias('oradea', 'bucarest', 380)
    distancias.add_distancias('pitesti', 'bucarest', 100)
    distancias.add_distancias('rimmicu', 'bucarest', 193)
    distancias.add_distancias('sibiu', 'bucarest', 253)
    distancias.add_distancias('timisoara', 'bucarest', 329)
    distancias.add_distancias('urziceni', 'bucarest', 80)
    distancias.add_distancias('vaslui', 'bucarest', 199)
    distancias.add_distancias('zerind', 'bucarest', 374)

    print(
        busca_a_estrela(cities, 'arad', 'bucarest', distancias)
    )
