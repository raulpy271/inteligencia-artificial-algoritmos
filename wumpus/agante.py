
from random import choice

from definitions import *

def find_hero(gameboard):
    size = len(gameboard)
    for line in range(size):
        for col in range(size):
            if HERO_TYPE in gameboard[line][col]:
                return line, col
    return -1, -1

class Agent:

    def hero_wins(self, gameboard):
        line, col = find_hero(gameboard)
        return OURO_TYPE in gameboard[line][col]

    def hero_lost(self, gameboard):
        line, col = find_hero(gameboard)
        return BURACO_TYPE in gameboard[line][col] or WUNPUS_TYPE in gameboard[line][col]

    def move_hero(self, gameboard, action):
        size = len(gameboard)
        line, col = find_hero(gameboard)
        if line == -1:
            print('Hero dont found')
            return
        if action == DOWN:
            if line < size  - 1:
                gameboard[line + 1][col] = gameboard[line + 1][col] + HERO_TYPE
            else:
                return
        elif action == UP:
            if line > 0:
                gameboard[line - 1][col] = gameboard[line - 1][col] + HERO_TYPE
            else:
                return
        elif action == RIGHT:
            if col <  size - 1:
                gameboard[line][col + 1] = gameboard[line][col + 1] + HERO_TYPE
            else:
                return
        elif action == LEFT:
            if col > 0:
                gameboard[line][col - 1] = gameboard[line][col - 1] + HERO_TYPE
            else:
                return
        else:
            raise Exception('Invalid action ' + action)
        gameboard[line][col] = gameboard[line][col].replace(HERO_TYPE, EMPTY_TYPE)

    def next_action(self, gameboard):
        next_action = choice([UP, DOWN, RIGHT, LEFT])
        self.move_hero(gameboard, next_action)
