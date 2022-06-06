from time import sleep
from os import system
from random import randint

from definitions import *
from agante import Agent

def print_board(gameboard):
    lines_str = map(lambda line: '|' + ('\t|'.join(line)) + '\t|', gameboard)
    result = '\n'.join(lines_str)
    system('clear')
    print(result)

def generate_random_position(size):
    line = randint(0, size - 1)
    col = randint(0, size - 1)
    return line, col

def create_empty_gameboard(size):
    empty_line = [EMPTY_TYPE] * size
    gameboard = []
    for _ in range(size):
        gameboard.append(empty_line.copy())
    return gameboard

def empty_position(gameboard, line, col):
    return gameboard[line][col] == EMPTY_TYPE

def insert_a_random_item(gameboard, item_type):
    while True:
        line, col = generate_random_position(len(gameboard))
        if empty_position(gameboard, line, col):
            gameboard[line][col] = item_type 
            break
    
def create_gameboard(size):
    gameboard = create_empty_gameboard(size)
    gameboard[0][0] = HERO_TYPE
    insert_a_random_item(gameboard, WUNPUS_TYPE)
    insert_a_random_item(gameboard, BURACO_TYPE)
    insert_a_random_item(gameboard, OURO_TYPE)
    return gameboard

def run_game():
    size = 4
    game = create_gameboard(size)
    agente = Agent()
    while True:
        print_board(game)
        if agente.hero_wins(game):
            print('Hero wins!')
            return
        elif agente.hero_lost(game):
            print('Hero lost!')
            return
        agente.next_action(game)
        sleep(0.5)

if __name__ == '__main__':
    run_game()

