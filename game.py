import random

from algorithms import Minimax, AlphaBeta
from state import State
from utils import pretty_print


class Game:
    def __init__(self, algorithm="alpha_beta"):
        self._state = State()
        self._tics = {0: "x", 1: "o"}
        self._who_am_i = {0: "human", 1: "cpu"}
        self._algorithm = (Minimax if algorithm == "minimax" else AlphaBeta)()

    def move(self, board, who: int):
        if who == 0:
            valid_positions = self._state.valid_positions
            position = int(input(f"Put position... {valid_positions}: "))
            while position not in range(9) or not self.is_valid_movement(board, position):
                position = int(input(f"Please, put a valid position... {valid_positions}: "))
        else:
            position = self._algorithm.run(self._state)

        self._state = State(
            board=board[:position] + self._tics.get(who) + board[position + 1 :], player=self._tics.get(int(not who))
        )

    def is_valid_movement(self, board, position):
        return board[position] == "-"

    def random_start(self):
        return random.randint(0, 1)

    def game_cycle(self):
        """Fully game cycle"""

        who = self.random_start()
        print(pretty_print(self._state.board))
        while not self._state.is_terminal:
            who = int(not who)
            print(f"Turn for {self._who_am_i.get(who)} player")
            self.move(self._state.board, who=who)
            print(pretty_print(self._state.board))

        print("Game finished!")


if __name__ == "__main__":
    game = Game()
    game.game_cycle()
