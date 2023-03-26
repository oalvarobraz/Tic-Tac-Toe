from gameBoard import StatusPlace


class GameMove:

    def __init__(self, vertical: int, horizontal: int, simbol: StatusPlace):
        self.vertical = vertical
        self.horizontal = horizontal
        self.simbol = simbol

    def move(self, vertical: int, horizontal: int, player: StatusPlace, board):
        if 0 > vertical > 3 or 0 > horizontal > 3:
            return -1
        else:
            return board.insert(vertical, horizontal, player)
