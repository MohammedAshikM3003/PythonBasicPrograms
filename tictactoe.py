# Tic Tac Toe Game in Python
# Author: ChatGPT

def print_board(board):
    """Display the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """Check if a player has won."""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    """Check if the game is a draw."""
    return all(space != " " for space in board)

def play_game():
    """Main game loop."""
    board = [" "] * 9
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is 'X' and Player 2 is 'O'")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move! Please choose a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[move] = current_player
            print_board(board)

            # Check for win
            if check_winner(board, current_player):
                print(f"Player {current_player} wins! 🎉")
                break

            # Check for draw
            if is_draw(board):
                print("It's a draw! 🤝")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    play_game()
