__author__ = 'Shelly'

from board import Board

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

    def run(self):
        while not self.board.check_win():
            self._turn_logic()

    @classmethod
    def play(cls, value1=X, value2=O):
        game = cls(value1, value2)
        game.run()


class HumanVsHumanGame(Game):
    def _turn_logic(self):
        row, col = self._get_index()
        self.board.set_cell_value(row, col, self._current_value)
        self._current_value = self._next_value
        print
        print self.board
        print

if __name__ == '__main__':
    Game().run()