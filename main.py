from models.Board import Board
from models.Player import Player

if __name__ == '__main__':
    board = Board()
    player1 = Player('y')
    player2 = Player('x')

    while board.x_keys_qtd > 0 and board.y_keys_qtd > 0:
        player = player2 if board.round % 2 == 0 else player1

        board.print_info(player)

        [piece_pos_x, piece_pos_y, pos_x, pos_y] = map(
            int,
            input("Insert position of piece as: piece_pos_x, piece_pos_y, pos_to_x, pos_to_y\n").split(" ")
        )

        board.walk_keys_to_pos(piece_pos_x, piece_pos_y, pos_x, pos_y, player)
