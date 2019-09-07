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

    def create_keys(self, start, end, piece):
        board_copy = self.BOARD[start:end]
        for index_row, row in enumerate(board_copy):
            for index_cell, cell in enumerate(row):
                if index_row % 2 == 0:
                    if index_cell % 2 == 0:
                        board_copy[index_row][index_cell] = piece
                else:
                    if index_cell % 2 != 0:
                        board_copy[index_row][index_cell] = piece

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
        valid_piece = not self.check_place_is_empty(piece_x, piece_y)
        valid_position = self.check_walk_position_is_valid(piece_x, piece_y, pos_x, pos_y)
        is_empty = self.check_place_is_empty(pos_x, pos_y)
        is_position_available = [pos_x, pos_y] in self.positions_available_to_walk(piece_x, piece_y)

        if not valid_piece:
            print("There's no piece in the given position")
            print("Try again")
            return

        if not valid_position:
            print("Invalid position to walk")
            print("Try again")
            return

        if not is_empty:
            print("There's a piece in the location that you want to move")
            print("Try again")
            return

        if not is_position_available:
            print("Invalid position to walk")
            print("try again")
            return

        key = self.BOARD[piece_y][piece_x]
        self.BOARD[piece_y][piece_x] = ' '
        self.BOARD[pos_y][pos_x] = Piece(key.format)

    def get_position_available_piece_not_queen(self, pos_x, pos_y, piece):
        if self.check_place_is_empty(pos_x, pos_y):
            return [pos_x, pos_y]
        elif self.check_place_is_empty(pos_x + 1, pos_y + 1) and self.get_piece_at_position(pos_x, pos_y) != piece.format:
            return [pos_x + 1, pos_y + 1]


    def get_position_available(self, pos_x, pos_y, piece, fn):
        if not piece.has_crown():
            return self.get_position_available_piece_not_queen(
                pos_x,
                pos_y,
                piece
            )

        if not self.check_position_is_valid(pos_x, pos_y):
            return []

        new_pos_x, new_pos_y = fn(pos_x, pos_y)
        return self.get_position_available(new_pos_x, new_pos_y, piece, fn).push([pos_x, pos_y])

    def positions_available_to_walk(self, piece_x, piece_y):
        piece = self.BOARD[piece_y][piece_x]
        available_positions = []
        if piece != ' ' and not piece.has_crown():
            if piece.format == 'x':
                available_positions.append(self.get_position_available(
                    piece_x + 1,
                    piece_y + 1,
                    piece,
                    lambda pos_x, pos_y: (pos_x + 1, pos_y + 1)
                ))
                available_positions.append(self.get_position_available(
                    piece_x - 1,
                    piece_y + 1,
                    piece,
                    lambda pos_x, pos_y: (pos_x - 1, pos_y + 1)
                ))

            elif piece.format == 'y':
                available_positions.append(self.get_position_available(
                    piece_x + 1,
                    piece_y - 1,
                    piece,
                    lambda pos_x, pos_y: (pos_x + 1, pos_y - 1)
                ))
                available_positions.append(self.get_position_available(
                    piece_x - 1,
                    piece_y - 1,
                    piece,
                    lambda pos_x, pos_y: (pos_x - 1, pos_y - 1)
                ))
        return available_positions

    def get_piece_at_position(self, pos_x, pos_y):
        return self.BOARD[pos_y][pos_x]

    def check_place_is_empty(self, pos_x, pos_y):
        return self.BOARD[pos_y][pos_x] == ' '

    def check_walk_position_is_valid(self, piece_x, piece_y, pos_x, pos_y):
        valid = []
        valid.append(self.check_position_is_valid(pos_x, pos_y))
        valid.append(piece_x != pos_x)
        valid.append(piece_y != pos_y)
        if ((piece_x < pos_x) and (piece_y < pos_y)) or ((piece_x > pos_x) and (piece_y > pos_y)):
            valid.append(piece_x - piece_y == pos_x - pos_y)
        elif ((piece_x < pos_x) and (piece_y > pos_y)) or ((piece_x > pos_x) and (piece_y < pos_y)):
            valid.append(piece_x + piece_y == pos_x + pos_y)
        return not False in valid

    def check_position_is_valid(self, pos_x, pos_y):
        return pos_y > -1 \
            and pos_y < 8 \
            and pos_x > -1 \
            and pos_x < 8

