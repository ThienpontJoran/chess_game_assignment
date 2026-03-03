from pieces import Pawn, Rook, Bishop, Knight, Queen, King, Board


board = Board()

# Create pawns
white_pawn = Pawn("WHITE", 1)
black_pawn = Pawn("BLACK", 1)

# Place pawns
board.place_piece(white_pawn, "e2")
board.place_piece(black_pawn, "e7")

print("Initial Board:")
board.print_board()

print("\nWhite pawn moves:")
white_pawn.move()
board.print_board()

print("\nBlack pawn moves:")
black_pawn.move()
board.print_board()