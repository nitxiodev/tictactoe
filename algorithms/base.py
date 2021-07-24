from state import State


class Algorithm:
    """Main class to implement minimax-like algorithms"""

    infinite = 1000

    def successors(self, state: State) -> list:
        """Return the list of successors for given state"""

        action_list = []
        for index, value in enumerate(state.board):
            if value == "-":
                board = state.board[:]
                board = board[:index] + state.player + board[index + 1 :]
                action_list.append(State(board=board, player=state.next_player, movement=index))

        return action_list

    def min_value(self, state: State, *args, **kwargs) -> int:
        """Step pass for minimax-like algorithms"""
        raise NotImplementedError("Not implemented yet!")

    def max_value(self, state: State, *args, **kwargs) -> int:
        """Step pass for minimax-like algorithms"""
        raise NotImplementedError("Not implemented yet!")

    def run(self, state: State):
        """Minimax main logic"""
        return max(enumerate(self.successors(state)), key=lambda x: self.min_value(x[1], -1000, 1000))[1].movement
