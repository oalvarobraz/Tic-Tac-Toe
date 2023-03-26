from gameBoard import Board
from gameMove import GameMove
from gameBoard import StatusPlace


def show_board(board: Board):
    print("\n")
    for i in range(board.height):
        for j in range(board.width):
            print(f" {board.board[i][j]} ", end="")
            if j != (board.width - 1):
                print("|", end="")
        print("")
        if i != (board.height - 1):
            print("-----------")
    print("\n")


def start_game():
    board = Board()
    mov = GameMove(-1, -1, StatusPlace.EMPTY)
    print("Choice or simbol: ")
    choice = input("|| Player one: (X or O): ")
    if choice.upper() == "X":
        player_one = StatusPlace.X
        player_two = StatusPlace.O
    else:
        player_one = StatusPlace.O
        player_two = StatusPlace.X

    while 1:
        show_board(board)
        print("|| Player 1")
        coord = input("|| Informe as coordenadas (x,y): ")
        moviment_x, moviment_y = map(int, coord.split(","))

        mov_1 = mov.move(moviment_x, moviment_y, player_one, board)

        while mov_1 == -1:
            print("|| Player 1")
            coord = input("|| Informe as coordenadas novamente (x,y): ")
            moviment_x, moviment_y = map(int, coord.split(","))
            mov_1 = mov.move(moviment_x, moviment_y, player_one, board)

        show_board(board)
        if board.has_winner() != StatusPlace.EMPTY:
            print("|| Player 1 is the winner")
            break

        print("|| Player 2")
        coord = input("|| Informe as coordenadas (x,y): ")
        moviment_x, moviment_y = map(int, coord.split(","))

        mov_2 = mov.move(moviment_x, moviment_y, player_two, board)

        while mov_2 == -1:
            print("|| Player 2")
            coord = input("|| Informe as coordenadas novamente (x,y): ")
            moviment_x, moviment_y = map(int, coord.split(","))
            mov_2 = mov.move(moviment_x, moviment_y, player_two, board)

        if board.has_winner() != StatusPlace.EMPTY:
            show_board(board)
            print("|| Player 2 is the winner")
            break

        if board.is_full() == 1:
            board.reset_board()
