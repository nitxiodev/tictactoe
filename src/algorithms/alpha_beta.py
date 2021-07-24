from src.algorithms.base import Algorithm
from src.state import State


class AlphaBeta(Algorithm):
    """Basic minimax algorithm based on Rusell&Norvig pseudocode"""

    def max_value(self, state: State, alpha: int, beta: int):
        """Max value function for minimax algorithm"""

        if state.is_terminal:
            return state.utility

        v = -self.infinite
        for action in self.successors(state):
            v = max(v, self.min_value(action, alpha, beta))
            if alpha >= beta:
                return v
            alpha = max(alpha, v)

        return v

    def min_value(self, state: State, alpha: int, beta: int):
        """Min value function for minimax algorithm"""

        if state.is_terminal:
            return state.utility

        v = self.infinite
        for action in self.successors(state):
            v = min(v, self.max_value(action, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
