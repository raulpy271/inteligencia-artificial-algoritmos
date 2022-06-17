
from sys import argv

from main_a_estrela import executa_busca_exemplo as executa_busca_a_estrela
from main_busca_em_profundidade import executa_busca_exemplo as executa_busca_em_profundidade

if __name__ == '__main__':
    numero_de_execucoes = 100000
    metodo = argv[1]
    if metodo == 'a_estrela':
        busca_metodo = executa_busca_a_estrela
    elif metodo == 'em_profundidade':
        busca_metodo = executa_busca_em_profundidade
    else:
        raise Exception(f'Método não suportado {metodo}')

    for _ in range(numero_de_execucoes):
        busca_metodo()
