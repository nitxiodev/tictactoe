from dataclasses import dataclass


@dataclass
class State:
    board: str = "-" * 9
    player: str = "x"
    payoff: int = 0
    movement: int = None

    def __repr__(self):
        return f"State(board={self.board}, movement={self.movement}, payoff={self.payoff}, player={self.player})"

    @property
    def next_player(self):
        return "x" if self.player == "o" else "o"

    def _update_payoff(self):
        self.payoff = 1 if self.player == "x" else -1

    @property
    def is_terminal(self):
        """This state will be terminal iff one player has fulfill a row/column/diagonal or board is full"""

        def check_rows():
            for index in range(3):
                row = self.board[index * 3 : (index * 3) + 3]
                if all([character == row[0] and "-" not in row for character in row]):
                    # Set utility function
                    self._update_payoff()
                    return True
            return False

        def check_cols():
            for index in range(3):
                column = [self.board[index + (index_ * 3)] for index_ in range(3)]
                if all([character == column[0] and "-" not in column for character in column]):
                    # Set utility function
                    self._update_payoff()
                    return True
            return False

        def check_diagonals():
            diagonals_board = [[self.board[index * 3 + index] for index in range(3)]] + [
                [self.board[index * 2 + 2] for index in range(3)]
            ]
            for diagonal in diagonals_board:
                if all([character == diagonal[0] and "-" not in diagonal for character in diagonal]):
                    # Set utility function
                    self._update_payoff()
                    return True
            return False

        def check_full():
            return "-" not in self.board

        return check_full() or check_rows() or check_cols() or check_diagonals()

    @property
    def utility(self):
        return self.payoff

    @property
    def valid_positions(self):
        return "".join([str(index) for index, value in enumerate(self.board) if value == "-"])
