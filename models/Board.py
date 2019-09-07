from models.Piece import Piece

# TODO: validate when piece has eaten;

class Board:
    def __init__(self):
        self.BOARD = [
            [
                ' ' for y in range(8)
            ] for x in range(8)
        ]
        self.x_keys_qtd = 12
        self.y_keys_qtd = 12
        self.create_keys(0, 3, Piece('x'))
        self.create_keys(5, None, Piece('y'))

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
        LINE = '|---' * 8
        for row in self.BOARD:
            string = '| '
            for cell in row:
                string += '{} | '.format(cell)
            print(LINE + '|')
            print(string)
        print(LINE + '|')

    def walk_keys_to_pos(self, piece_x, piece_y, pos_x, pos_y):
        valid_position = self.check_walk_position_is_valid(piece_x, piece_y, pos_x, pos_y)
        is_empty = self.check_place_is_empty(pos_x, pos_y)
        positions_available_to = self.positions_available_to(piece_x, piece_y)
        if valid_position and is_empty and [pos_x, pos_y] in positions_available_to:
            key = self.BOARD[piece_y][piece_x]
            self.BOARD[piece_y][piece_x] = ' '
            self.BOARD[pos_y][pos_x] = Piece(key.format)

    def positions_available_to(self, piece_x, piece_y):
        piece = self.BOARD[piece_y][piece_x]
        available_positions = []
        if not piece.has_crown():
            if piece.format == 'x':
                available_positions.append([piece_x + 1, piece_y + 1])
                available_positions.append([piece_x - 1, piece_y + 1])
            elif piece.format == 'y':
                available_positions.append([piece_x + 1, piece_y - 1])
                available_positions.append([piece_x - 1, piece_y - 1])
        return available_positions

    def check_place_is_empty(self, pos_x, pos_y):
        return self.BOARD[pos_y][pos_x] == ' '

    def check_walk_position_is_valid(self, piece_x, piece_y, pos_x, pos_y):
        return piece_x != pos_x \
            and piece_y != pos_y \
            and pos_y > -1 \
            and pos_x > -1 \
            and pos_y < 8 \
            and pos_x < 8

