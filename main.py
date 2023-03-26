import game

if __name__ == '__main__':
    print("Welcome to the Hash game!")
    keep_playing = True

    while keep_playing:
        game.start_game()
        play_again = input("Do you want to play again? (S/N): ").strip().lower()
        while play_again not in ('s', 'n'):
            play_again = input("Type S to continue or N to get out: ").strip().lower()
        keep_playing = play_again == 's'
    print("Thanks for playing!")
