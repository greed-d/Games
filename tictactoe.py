# board
# display
# PlayGame
# HandleTurn
# CheckWin
# CheckRow
# CheckColumn
# CheckDiagonal
# CheckTie
# FlipPlayer

#   ------Global Variables-----

# Game Board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Whose turn is it?
current_player = "X"

play_again = 'yes'


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe


def play_game():

    # Displaying intial board
    display_board()

    # While the game is still going
    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if game has ended
        check_if_GameOver()

        # Flipping player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


# Handle a single turn
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose the positon from 1-9: ")

    valid = False
    while not valid:

        # Code for invalid input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Choose the positon from 1-9: ")

        # Casting string into an integer and reducing the place to match input
        position = int(position) - 1

        # To make player choose another slot
        if board[position] == "-":
            valid = True
            print("You can't enter at this place!!. Please choose another slot. :)")

    board[position] = player
    display_board()


# Check if game is over
def check_if_GameOver():
    check_if_win()
    check_if_tie()


def check_rows():
    global game_still_going

    # Check if any of the row has same value (not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match flag that as a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():

    global game_still_going

    # Check if any of the column has same value (not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match flag that as a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():

    # Global function for game still going
    global game_still_going

    # Check if any of the diagonal has same value (not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal does have a match flag that as a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

    return


def play_again_2():
    print("Do you want to play again?")
    input().lower().startswith('y')
    return

# Check if player1 or player2 has won


def check_if_win():

    global winner

    # Check Rows
    row_winner = check_rows()

    # Check Columns
    colum_winner = check_columns()

    # Check Diags
    diagonal_winner = check_diagonals()

    # To check if player won by row, column or diagonal
    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


# Check if none of the player has won
def check_if_tie():

    # Global variable we need
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return


# To flip between "X" and "O"
def flip_player():

    # Global variable we need
    global current_player

    # When current player is "X"
    if current_player == "X":
        current_player = "O"

    # When current player is "O"
    elif current_player == "O":
        current_player = "X"
    return


# Function call to play the game
play_game()
