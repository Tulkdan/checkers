from models.Board import Board
from models.Player import Player

if __name__ == '__main__':
    board = Board()
    turno = 1;

    while board.x_keys_qtd > 0 and board.y_keys_qtd > 0:
        board.print_board()
        
        if turno % 2 == 0:
            player = Player('2')
            print("Player 2 ")
            
        else:
            player = Player('1')
            print("Player 1 ")

        [piece_pos_x, piece_pos_y, pos_x, pos_y] = map(int, input(
            "Insert position of piece as: piece_pos_x, piece_pos_y, pos_to_x, pos_to_y\n").split(" "))
        if board.walk_keys_to_pos(piece_pos_x, piece_pos_y, pos_x, pos_y, player.format) is True:
            turno = turno + 1
