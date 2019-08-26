LINE = '|---' * 8

class Board:
    def __init__(self):
        self.BOARD = [
            [
                0 for y in range(8)
            ] for x in range(8)
        ]
        self.x_keys_qtd = 12
        self.y_keys_qtd = 12
        self.create_keys(0, 3, 'X')
        self.create_keys(5, None, 'Y')

    def create_keys(self, start, end, key):
        board_copy = self.BOARD[start:end]
        for index_row, row in enumerate(board_copy):
            for index_cell, cell in enumerate(row):
                if index_row % 2 == 0:
                    if index_cell % 2 == 0:
                        board_copy[index_row][index_cell] = key
                else:
                    if index_cell % 2 != 0:
                        board_copy[index_row][index_cell] = key

    def print_board(self):
        for row in self.BOARD:
            string = '| '
            for cell in row:
                string += '{} | '.format(cell)
            print(LINE + '|')
            print(string)
        print(LINE + '|')

    def walk_keys_to_pos(self, piece_x, piece_y, pos_x, pos_y):
        if self.check_walk_position_is_valid(piece_x, piece_y, pos_x, pos_y):
            key = self.BOARD[piece_y][piece_x]
            self.BOARD[piece_y][piece_x] = '0'
            self.BOARD[pos_y][pos_x] = key

    def check_walk_position_is_valid(self, piece_x, piece_y, pos_x, pos_y):
        return piece_x != pos_x \
            and piece_y != pos_y \
            and pos_y >= 0 \
            and pos_x >= 0 \
            and pos_y < 8 \
            and pos_x < 8


if __name__ == '__main__':
    board = Board()

    while board.x_keys_qtd > 0 and board.y_keys_qtd > 0:
        board.print_board()
        [piece_pos_x, piece_pos_y, pos_x, pos_y] = map(int, input("Insert position of piece as: piece_pos_x, piece_pos_y, pos_to_x, pos_to_y\n").split(" "))
        board.walk_keys_to_pos(piece_pos_x, piece_pos_y, pos_x, pos_y)

