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
    def move(self, movement):
        print(movement)

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return f"{self.color} {self.name} {self.identifier}"
    


class Pawn(BaseChessPiece):

    def __init__(self, color:str, identifier:int):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        movement = "Pawn moves forward 1 position"
        super().move(movement)


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