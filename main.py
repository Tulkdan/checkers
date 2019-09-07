from models.Board import Board

if __name__ == '__main__':
    board = Board()

    while board.x_keys_qtd > 0 and board.y_keys_qtd > 0:
        board.print_board()
        [piece_pos_x, piece_pos_y, pos_x, pos_y] = map(int, input("Insert position of piece as: piece_pos_x, piece_pos_y, pos_to_x, pos_to_y\n").split(" "))
        board.walk_keys_to_pos(piece_pos_x, piece_pos_y, pos_x, pos_y)

