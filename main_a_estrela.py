
from busca_A_estrela.busca import busca_a_estrela, obtem_proximo_no_usando_heuristica
from utils.graph import Graph
from utils.plano_cartesiano import PlanoCartesiano

def executa_busca_exemplo():
    cities = Graph()
    plano = PlanoCartesiano()
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

    plano.add_pontos('arad', 20, 75)
    plano.add_pontos('timisoara', 25, 45)
    plano.add_pontos('zerind', 30, 85)
    plano.add_pontos('oradea', 40, 100)
    plano.add_pontos('lugoj', 50, 40)
    plano.add_pontos('mehadia', 50, 25)
    plano.add_pontos('brobeta', 50, 10)
    plano.add_pontos('craiova', 75, 5)
    plano.add_pontos('sibiu', 60, 65)
    plano.add_pontos('rimmicu', 70, 50)
    plano.add_pontos('pitesti', 100, 35)
    plano.add_pontos('fagaras', 95, 60)
    plano.add_pontos('bucarest', 125, 20)

    return busca_a_estrela(cities, 'arad', 'bucarest', plano)

if __name__ == '__main__':

    print(
        executa_busca_exemplo()
    )
