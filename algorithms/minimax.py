from algorithms.base import Algorithm
from state import State


class Minimax(Algorithm):
    """Basic minimax algorithm based on Rusell&Norvig pseudocode"""

    def max_value(self, state: State) -> int:
        if state.is_terminal:
            return state.utility

        v = -self.infinite
        for action in self.successors(state):
            v = max(v, self.min_value(action))

        return v

    def min_value(self, state: State) -> int:
        if state.is_terminal:
            return state.utility

        v = self.infinite
        for action in self.successors(state):
            v = min(v, self.max_value(action))
        return v
