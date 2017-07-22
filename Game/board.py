__author__ = 'Shelly'

class Board(object):
    def __init__(self):
        self.cells = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def __getitem__(self, item):
        return self.cells[item]

    def _get_rows(self):
        return self.cells

    def _get_columns(self):
        return [[j[i] for j in self.cells] for i in xrange(len(self.cells))]

    def _get_diagonals(self):
        return [
            [self.cells[i][i] for i in xrange(len(self.cells))],
            [self.cells[i][len(self.cells) - 1 - i] for i in xrange(len(self.cells))]
        ]

    def _get_all_sequences(self):
        return self._get_rows() + self._get_columns() + self._get_diagonals()

    @staticmethod
    def _is_win_sequence(seq):
        seq_set = set(seq)
        return len(seq_set) == 1 and seq_set.pop() is not None

    def check_win(self):
        return any(map(self._is_win_sequence, self._get_all_sequences()))

    def __repr__(self):
        return "\n".join(['|'.join(map(lambda val: val or '_', row)) for row in self.cells])
