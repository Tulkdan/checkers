from models.Board import Board
from models.Player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('y')
        self.player2 = Player('x')

    def start_game(self):
        while self.board.x_keys_qtd > 0 and self.board.y_keys_qtd > 0:
            player = self.player2 if self.board.round % 2 == 0 else self.player1

            self.board.print_info(player)

            [piece_pos_x, piece_pos_y, pos_x, pos_y] = map(
                int,
                input("Insert position of piece as: piece_pos_x, piece_pos_y, pos_to_x, pos_to_y\n").split(" ")
            )

            self.board.walk_keys_to_pos(piece_pos_x, piece_pos_y, pos_x, pos_y, player)
