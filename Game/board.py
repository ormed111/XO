__author__ = 'ormed'

DEFAULT_BOARD_SIZE = 3


class Cell(object):
    def __init__(self, row_index, col_index, value):
        self.x = row_index
        self.y = col_index
        self.value = value

    def __repr__(self):
        return "[{x},{y}]={val}".format(x=self.x, y=self.y, val=self.value)


class Board(object):
    _EMPTY_CELL_VALUE = None

    def __init__(self, size=DEFAULT_BOARD_SIZE):
        self.size = size
        self._initiate_cells()

    def _initiate_cells(self):
        self.cells = [[Cell(i, j, self._EMPTY_CELL_VALUE) for j in xrange(self.size)] for i in xrange(self.size)]

    def __getitem__(self, item):
        return self.cells[item]

    def set_cell_value(self, row_index, col_index, value):
        self.cells[row_index][col_index].value = value

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
        seq_set = set(map(lambda cell: cell.value, seq))
        return len(seq_set) == 1 and seq_set.pop() is not None

    def check_win(self):
        return any(map(self._is_win_sequence, self._get_all_sequences()))

    def get_empty_cells(self):
        return [cell for row in self.cells for cell in row if cell.value == self._EMPTY_CELL_VALUE]

    def __repr__(self):
        return "\n".join(['|'.join(map(lambda cell: cell.value or '_', row)) for row in self.cells])
