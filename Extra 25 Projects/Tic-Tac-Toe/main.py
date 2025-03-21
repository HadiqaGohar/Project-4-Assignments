import time

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            row, col = map(int, input(f"Player {players[current_player]}, enter row and column (0-2, space-separated): ").split())

            if board[row][col] == " ":
                board[row][col] = players[current_player]
                print_board(board)

                if check_winner(board, players[current_player]):
                    print(f"🎉 Player {players[current_player]} wins!")
                    break

                if is_full(board):
                    print("It's a tie! 🤝")
                    break

                current_player = 1 - current_player  # Switch player
                time.sleep(1)
            else:
                print("That spot is already taken. Try again!")

        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers between 0 and 2.")

# Run the game
if __name__ == "__main__":
    play_game()
