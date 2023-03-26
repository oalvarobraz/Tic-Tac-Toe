class StatusPlace:
    EMPTY = " "
    X = "X"
    O = "O"


class Board:
    def __init__(self, width: int = 3, height: int = 3):
        self.width = width
        self.height = height
        self.board = []

        # Criando o tabuleiro vazio
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(StatusPlace.EMPTY)
            self.board.append(row)

    def is_full(self):
        return all(self.board[i][j] != StatusPlace.EMPTY for i in range(self.width) for j in range(self.height))

    def get_status(self, x: int, y: int):
        if x >= self.width or y >= self.height:
            print(f"Error: Value is out of limit {self.width}")
            return -1
        return self.board[x][y]

    def insert(self, x: int, y: int, player: StatusPlace):
        a = self.get_status(x, y)
        if self.get_status(x, y) == StatusPlace.EMPTY:
            self.board[x][y] = player
            return 1
        else:
            return -1

    def check_lines(self):
        for i in range(self.width):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        return StatusPlace.EMPTY

    def check_coluns(self):
        for j in range(self.height):
            if self.board[0][j] == self.board[1][j] == self.board[2][j]:
                return self.board[0][j]
        return StatusPlace.EMPTY

    def check_diagnals(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return StatusPlace.EMPTY

    def has_winner(self):
        lines = self.check_lines()
        coluns = self.check_coluns()
        diagnals = self.check_diagnals()
        if lines != StatusPlace.EMPTY:
            return lines
        elif coluns != StatusPlace.EMPTY:
            return coluns
        elif diagnals != StatusPlace.EMPTY:
            return diagnals
        return StatusPlace.EMPTY

    def reset_board(self):
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(StatusPlace.EMPTY)
            self.board.append(row)
