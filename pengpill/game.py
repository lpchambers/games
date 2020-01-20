#!/usr/bin/python3
from pill import PILL_ORDER
from async_utils import AsyncLoopingCall

class Game:
    def __init__(self):
        self.pills = [PILL_ORDER[0]]
        self.pill_next = 1
        self.currency = 0
        self.game_loop = AsyncLoopingCall(self.game_iter)

    def start(self):
        # Start 1 second interval
        self.game_loop.start(1, now=False)

    def stop(self):
        self.game_loop.stop()

    @property
    def income(self):
        return sum(pill.income for pill in self.pills)

    def click_pill(self, pill):
        """
        Pill is the index of pill to click
        """
        if pill < len(self.pills):
            return self.pills[pill].click()
        else:
            return f"No pill {pill} found?"

    def game_iter(self):
        self.currency += self.income


import os
import time
def draw_state(game):
    os.system('clear')
    print(f"Peng Pill The Game")
    print(f"  Build your peng empire")
    print()
    print(f"Peng Bucks: {game.currency}")
    print(f"Income: {game.income}")
    for idx, pill in enumerate(game.pills):
        print()
        print(f"Pill {idx}")
        pill.render()


def ask_inputs():
    pass


def main():
    g = Game()
    while True:
        draw_state(g)
        time.sleep(1)

