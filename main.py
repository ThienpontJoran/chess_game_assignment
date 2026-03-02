from pieces import Pawn, Rook, Bishop, Knight, Queen, King, Board


board = Board()
board.print_board()

pawn = board.find_piece("-", 1, "WHITE")
print(pawn)  # WHITE Pawn #1

board.kill_piece("a2")  # kills the WHITE pawn #1
board.print_board()