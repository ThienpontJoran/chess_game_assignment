from pieces import Pawn, Rook, Bishop, Knight, Queen, King, Board


board = Board()
board.print_board()

# Move a WHITE pawn forward
white_pawn = board.find_piece("-", 1, "WHITE")
white_pawn.move()
board.print_board()

# Move a BLACK pawn forward
black_pawn = board.find_piece("-", 1, "BLACK")
black_pawn.move()
board.print_board()

# Move WHITE pawn to capture BLACK pawn
white_pawn.move()  # assuming next square has black pawn
board.print_board()