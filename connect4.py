# Connect 4 by Aena Teodocio
# A classic strategy game where players battle to own the grid! Players choose "X" or "O" to represent their piece.
# They drop the piece into the grid, starting in the middle or at the edge.
# Use strategy to block opponents while aiming to be the first player to win by getting 4 pieces in a row.
# You win by stacking 4 pieces in a row vertically, horizontally, or diagonally!


def make_a_move(board, curr_player, empty_col):
    """Takes in the board (nested list), current player (string) and available columns (list of ints).
        It asks for user input from the list of ints representing the column to drop their piece in.
        If the input is not an available column, it exits out of function and re-calls make_a_move."""

    # ask for column to drop piece in
    try:
        col = int(input("It's {}'s turn. Please select a column. Your options are {}: ".format(curr_player, empty_col)))
    except ValueError:
        return make_a_move(board, curr_player, empty_col)

    while col not in empty_col:
        print("Trying to place an {} in column {}.".format(curr_player, col))
        print("Make sure to pick a column between 1 and 7 that is not full.")
        return make_a_move(board, curr_player, empty_col)

    # if valid answer, convert to zero index value
    col -= 1

    # updated nested list with the player's move. this "drops" their piece in a slot
    for row in board[-1::-1]:
        if row[col] == " ":
            row[col] = curr_player
            print("\n" + "Placed an {} in column {}.".format(curr_player, col + 1) + "\n")
            return board

        else:  # if slot is taken, find next row in the same column with empty slot
            continue


def check_winner(board, curr_player):
    """Takes in board (nested list) and current player (string).
        Checks if 4 pieces align horizontally, vertically, or diagonally.
        Returns a string if a winner exists or if the board is full but there's no winner.
        If neither is true, the game continues."""

    result = "Player {} wins!".format(curr_player)

    # Check for horizontal win
    for x in range(len(board)):
        for i in range(3):
            if board[x][i:i + 4].count(curr_player) == 4:
                return result

    # Check for vertical win
    for x in range(3):
        for y in range(len(board[0])):
            if board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 3][y] == curr_player:
                return result

    # Check for / diagonal win
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == board[x + 1][y - 1] == board[x + 2][y - 2] == board[x + 3][y - 3] == curr_player:
                return result

    # Check for \ diagonal win
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] == board[x + 3][y + 3] == curr_player:
                return result

    # No winner yet, now check if board is full
    count = 0
    for i in board:
        count += len(i)
    if count == 49:
        return "It's a tie. Game over!"

    # If all other checks are false, game is not over.
    return "Keep playing"


def create_board(curr_board):
    """Takes in a nested list that represents the game board.
        Returns a formatted board for user visualization of the game."""

    header = "  1   2   3   4   5   6   7"
    row_sep = "|---|---|---|---|---|---|---|"
    board = ''
    for row in curr_board:
        board += row_sep + "\n"
        for slot in row:
            board += ("| " + slot + " ")
        board += "|" + "\n"
    board += row_sep
    formatted_board = "\n" + header + "\n" + board + "\n"

    return formatted_board


def play_game(x_win=0, o_win=0):
    """Initializes the game.
        Default parameters: x_win, o_win are ints.
        Both parameters get updated when the first round ends and user wants to play again."""

    print("The game is ON!")

    curr_board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                  [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]
    x_move = 0
    o_move = 0

    game_status = "Keep playing"
    print(create_board(curr_board))

    while game_status == "Keep playing":

        # check if it's the other player's turn
        if x_move == o_move:
            player = "X"
            x_move += 1
        else:
            player = "O"
            o_move += 1

        # check for columns that are not yet full
        available_col = [i + 1 for i in range(len(curr_board[0])) if curr_board[0][i] == " "]

        # begin move selection and then check for a win
        curr_board = make_a_move(curr_board, player, available_col)
        game_status = check_winner(curr_board, player)

        # print formatted board after new moves are made

        print(create_board(curr_board))

        # if there's a winner, start win tally in case user wants to play again
        if "X" in game_status:
            x_win = 0
        else:
            o_win = 0
    print(game_status)
    return repeat_game(game_status, x_win, o_win)


def repeat_game(status, x_win, o_win):
    """Takes in a string (game status) and two ints (total # of wins for player x and o, respectively).
        Asks for user input whether to play again or not. If yes, it returns the win tally.
        If not, it exits out of the program completely."""

    play_again = input("Play again? Y or N: ")

    if play_again in "Yy":
        print("\n" + "Resuming the game!")
        return win_counter(status, x_win, o_win)

    elif play_again in "Nn":
        return "Thanks for playing, bye!!"

    else:  # in case of wrong input
        print("Please enter a valid answer.")
        return repeat_game(status, x_win, o_win)


def win_counter(winner, x_win, o_win):
    """"Takes in a string (winner) and two ints (total # of wins for player x and o, respectively).
        Prints the tally and re-calls play_game()."""
    x_score = x_win
    o_score = o_win

    # increment score count
    if "X" in winner:
        x_score += 1
    else:
        o_score += 1

    print("\n" + "~~~~~~~Winner's Tally~~~~~~~")
    print("        Player X: {} ".format(x_score))
    print("        Player O: {} ".format(o_score))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")

    return play_game(x_score, o_score)


print(play_game())
