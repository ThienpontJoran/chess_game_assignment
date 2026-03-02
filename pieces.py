from abc import ABC, abstractmethod
#test
class BaseChessPiece(ABC):

    def __init__(self, color: str, name: str, symbol: str, identifier: int):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = None
        self.is_alive = True
        self.board = None


    @abstractmethod
    def move(self, target_square: str):

        # Default logic to move on the board:
        if self.board is None:
            print("Board not defined for this piece")
            return

        new_location = self.board.squares.get(target_square)

        
        if new_location is None:
            print(f"{self} moves to {target_square}")
        else: 
            if new_location.color != self.color:
                print(f"{self} captures {new_location} at {target_square}")
                self.board.kill_piece(target_square)
            else:
                print(f"{self} cannot move to {target_square}, friendly piece there!")
                return

       
        self.board.squares[self.position] = None
        self.board.squares[target_square] = self
        self.position = target_square

    def set_position(self, square: str):
        self.position = square

    def define_board(self, board):
        self.board = board

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    


class Pawn(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        if self.position is None or self.board is None:
            print("Cannot move, piece not on board")
            return

        # Determine direction based on color
        row = int(self.position[1])
        col = self.position[0]
        new_row = row + 1 if self.color == "WHITE" else row - 1

        # Make sure pawn does not go off-board
        if new_row < 1 or new_row > 8:
            print(f"{self} cannot move off the board!")
            return

        target_square = f"{col}{new_row}"
        super().move(target_square)


class Rook(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Rook", "R", identifier)

    def move(self):
        movement = "Rook moves in a straight line"
        super().move(movement)


class Bishop(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self):
        movement = "Bishop moves diagonally"
        super().move(movement)


class Knight(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Knight", "N", identifier)

    def move(self):
        movement = "Knight moves in an L shape"
        super().move(movement)


class Queen(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "Queen", "Q", identifier)

    def move(self):
        movement = "Queen moves in all directions"
        super().move(movement)


class King(BaseChessPiece):

    def __init__(self, color: str, identifier: int):
        super().__init__(color, "King", "K", identifier)

    def move(self):
        movement = "King moves one square in any direction"
        super().move(movement)




class Board:

    def __init__(self):
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }

        self.setup_board()

    def print_board(self):
        for row in range(1, 9):
            row_squares = [
                self.squares[f"{chr(col)}{row}"]
                for col in range(ord('a'), ord('i'))
            ]
            print(row_squares)

    def setup_board(self):

        # BLACK major pieces (row 1)
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['e1'] = King('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['h1'] = Rook('BLACK', 2)

        # BLACK pawns (row 2)
        black_pawns = {
            f"{chr(col)}2": Pawn('BLACK', col - ord('a') + 1)
            for col in range(ord('a'), ord('i'))
        }

        self.squares.update(black_pawns)

        # WHITE major pieces (row 8)
        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['d8'] = Queen('WHITE', 1)
        self.squares['e8'] = King('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)
        self.squares['g8'] = Knight('WHITE', 2)
        self.squares['h8'] = Rook('WHITE', 2)

        # WHITE pawns (row 7)
        white_pawns = {
            f"{chr(col)}7": Pawn('WHITE', col - ord('a') + 1)
            for col in range(ord('a'), ord('i'))
        }

        self.squares.update(white_pawns)

    def move_piece(self, from_square, to_square):
        piece = self.squares[from_square]

        if piece is None:
            print(f"No piece at {from_square}")
            return

        # Check if target square has a piece
        target = self.squares[to_square]
        if target is not None:
            target.die()  # kill piece
            print(f"{piece} captures {target} at {to_square}")

        # Move piece
        self.squares[to_square] = piece
        self.squares[from_square] = None
        piece.set_position(to_square)

    def find_piece(self, symbol: str, identifier: int, color: str):

        pieces = [
            piece for piece in self.squares.values()
            if piece is not None
            and piece.symbol == symbol
            and piece.identifier == identifier
            and piece.color == color
        ]
        return pieces[0] if pieces else None
    

    def kill_piece(self, square: str):
  
        piece = self.squares.get(square)
        if piece:
            piece.die()          # mark piece as dead
            self.squares[square] = None
            print(f"{piece} has been killed at {square}")
        else:
            print(f"No piece to kill at {square}")


class BoardMovements:

    @staticmethod
    def forward(position: str, color: str, steps: int = 1) -> str:
        column = position[0]
        row = int(position[1])

        # White moves up, Black moves down
        new_row = row + steps if color == "WHITE" else row - steps

        # Stay inside board boundaries
        if new_row < 1:
            new_row = 1
        elif new_row > 8:
            new_row = 8

        return f"{column}{new_row}"

    @staticmethod
    def backward(position: str, color: str, steps: int = 1) -> str:
        # Just the opposite of forward
        return BoardMovements.forward(position, color, -steps)

    @staticmethod
    def left(position: str, steps: int = 1) -> str:
        column = chr(ord(position[0]) - steps)
        row = position[1]
        if column < 'a':
            column = 'a'
        return f"{column}{row}"

    @staticmethod
    def right(position: str, steps: int = 1) -> str:
        column = chr(ord(position[0]) + steps)
        row = position[1]
        if column > 'h':
            column = 'h'
        return f"{column}{row}"
        