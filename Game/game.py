__author__ = 'ormed'

from board import Board
from random import choice

X = 'X'
O = 'O'


class Game(object):
    def __init__(self, value1=X, value2=O):
        if value1 == value2:
            raise TypeError("Values cannot be the same")
        self._value1 = self._current_value = value1
        self._value2 = value2
        self.board = Board()

    @property
    def _next_value(self):
        return self._value1 if self._current_value == self._value2 else self._value2

    @staticmethod
    def _get_index():
        indexes = []
        while len(indexes) != 2:
            indexes = map(int, raw_input("Insert Index: ").strip().split(' '))
        return indexes

    def _turn_logic(self):
        raise NotImplementedError()

    def _print_board(self):
        print
        print self.board
        print

    def run(self):
        while not self.board.check_win():
            self._turn_logic()
            self._print_board()
            self._current_value = self._next_value

    @classmethod
    def play(cls, value1=X, value2=O):
        game = cls(value1, value2)
        game.run()


class HumanVsHumanGame(Game):
    def _turn_logic(self):
        row, col = self._get_index()
        self.board.set_cell_value(row, col, self._current_value)


class HumanVsComputerGame(Game):
    def _human_turn_logic(self):
        row, col = self._get_index()
        self.board.set_cell_value(row, col, self._current_value)

    def _computer_turn_logic(self):
        cell_to_insert = choice(self.board.get_empty_cells())
        self.board.set_cell_value(cell_to_insert.x, cell_to_insert.y, self._current_value)

    def _turn_logic(self): # just because i dont time for this now, the human will always go first and be value1
        if self._current_value == self._value1:
            self._human_turn_logic()
        else:
            self._computer_turn_logic()

if __name__ == '__main__':
    HumanVsComputerGame.play()
