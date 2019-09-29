from models.Piece import Piece

def message_error(message):
    print(f"Wait a minute, {message}")
    print("Try again")

class Board:
    def __init__(self):
        self.BOARD = [
            [Piece('x'), ' ', Piece('x'), ' ', Piece('x'), ' ', Piece('x'), ' '],
            [' ', Piece('x'), ' ', Piece('x'), ' ', Piece('x'), ' ', Piece('x')],
            [Piece('x'), ' ', Piece('x'), ' ', Piece('x'), ' ', Piece('x'), ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', Piece('y'), ' ', Piece('y'), ' ', Piece('y'), ' ', Piece('y')],
            [Piece('y'), ' ', Piece('y'), ' ', Piece('y'), ' ', Piece('y'), ' '],
            [' ', Piece('y'), ' ', Piece('y'), ' ', Piece('y'), ' ', Piece('y')],
        ]
        self.x_keys_qtd = 12
        self.y_keys_qtd = 12
        self.round = 1

    def print_info(self, player):
        self.print_board()
        self.print_round()
        print(f'--------- PLAYER {player.format} TURN ---------')


    def print_round(self):
        print(f'------------ ROUND {self.round} ------------')

    def print_board(self):
        output = ''
        LINE = '|---' * 8
        for row in self.BOARD:
            string = '| '
            for cell in row:
                string += '{} | '.format(cell)
            print(LINE + '|')
            print(string)
        print(LINE + '|')

    def walk_keys_to_pos(self, piece_x, piece_y, pos_x, pos_y, player):
        is_piece_valid_for_player = self.check_player_piece(player, piece_x, piece_y)
        valid_piece = not self.check_place_is_empty(piece_x, piece_y)
        valid_position = self.check_walk_position_is_valid(piece_x, piece_y, pos_x, pos_y)
        is_empty = self.check_place_is_empty(pos_x, pos_y)
        is_position_available = [pos_x, pos_y] in self.positions_available_to_walk(piece_x, piece_y)

        if not is_piece_valid_for_player:
            message_error("that's not your piece")
            return

        if not valid_piece:
            message_error("there's no piece in the given position")
            return

        if not valid_position:
            message_error("that's an invalid position to walk")
            return

        if not is_empty:
            message_error("there's a piece in the location that you want to move")
            return

        if not is_position_available:
            message_error("this position is invalid to walk")
            return

        all_squares = self.get_all_pieces_in_diagonal(piece_x, piece_y, pos_x, pos_y)
        if len(all_squares) and not self.remove_piece_if_had_jumped_houses(all_squares):
            message_error("we couldn't remove the piece")
            return

        key = self.BOARD[piece_y][piece_x]
        self.BOARD[piece_y][piece_x] = ' '
        self.BOARD[pos_y][pos_x] = Piece(key.format)
        self.round += 1

    def check_player_piece(self, player, pos_x, pos_y):
        piece = self.get_piece_at_position(pos_x, pos_y)
        return player.format == piece.format

    def remove_piece_if_had_jumped_houses(self, houses):
        valid = []
        for house in houses:
            valid.append(self.check_place_is_empty(house[0], house[1]))

        if valid.count(False) > 1:
            return False

        for house in houses:
            if not self.check_place_is_empty(house[0], house[1]):
                if self.get_piece_at_position(house[0], house[1]).format == 'x':
                    print("Removed a X piece")
                    self.x_keys_qtd -= 1
                else:
                    print("Removed a Y piece")
                    self.y_keys_qtd -= 1
                self.BOARD[house[1]][house[0]] = ' '
        print(self.x_keys_qtd, self.y_keys_qtd)
        return True

    def get_all_pieces_in_diagonal(self, origin_x, origin_y, pos_x, pos_y):
        diff_x = pos_x - origin_x
        diff_y = pos_y - origin_y
        fn = None
        if diff_x > 0:
            if diff_y > 0:
                fn = lambda pos_x, pos_y: (pos_x + 1, pos_y + 1)
            else:
                fn = lambda pos_x, pos_y: (pos_x + 1, pos_y - 1)
        else:
            if diff_y > 0:
                fn = lambda pos_x, pos_y: (pos_x - 1, pos_y + 1)
            else:
                fn = lambda pos_x, pos_y: (pos_x - 1, pos_y - 1)
        new_origin_x, new_origin_y = fn(origin_x, origin_y)
        return self.get_all_diagonal_places(new_origin_x, new_origin_y, pos_x, pos_y, fn)

    def get_all_diagonal_places(self, origin_x, origin_y, target_x, target_y, fn):
        if (origin_x == target_x and origin_y == target_y) or (origin_x < 0 or origin_y < 0):
            return []
        pos_x, pos_y = fn(origin_x, origin_y)
        result = self.get_all_diagonal_places(pos_x, pos_y, target_x, target_y, fn)
        result.append([origin_x, origin_y])
        return result

    def get_position_available_piece_not_queen(self, pos_x, pos_y, piece, fn):
        new_pos_x, new_pos_y = fn(pos_x, pos_y)
        if self.check_place_is_empty(pos_x, pos_y):
            return [pos_x, pos_y]
        elif self.check_place_is_empty(new_pos_x, new_pos_y) and self.get_piece_at_position(pos_x, pos_y) != piece.format:
            return [new_pos_x, new_pos_y]

    def get_position_available(self, pos_x, pos_y, piece, fn):
        if not piece.has_crown():
            return self.get_position_available_piece_not_queen(
                pos_x,
                pos_y,
                piece,
                fn
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
