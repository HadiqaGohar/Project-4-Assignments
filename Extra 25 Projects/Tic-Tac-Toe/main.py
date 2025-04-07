# # import time

# # # Function to print the board
# # def print_board(board):
# #     for row in board:
# #         print(" | ".join(row))
# #         print("-" * 9)

# # # Function to check for a win
# # def check_winner(board, player):
# #     # Check rows, columns, and diagonals
# #     for row in board:
# #         if all(cell == player for cell in row):
# #             return True

# #     for col in range(3):
# #         if all(board[row][col] == player for row in range(3)):
# #             return True

# #     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
# #         return True

# #     return False

# # # Function to check if the board is full
# # def is_full(board):
# #     return all(cell != " " for row in board for cell in row)

# # # Main game loop
# # def play_game():
# #     board = [[" " for _ in range(3)] for _ in range(3)]
# #     players = ["X", "O"]
# #     current_player = 0

# #     print("Welcome to Tic-Tac-Toe!")
# #     print_board(board)

# #     while True:
# #         try:
# #             row, col = map(int, input(f"Player {players[current_player]}, enter row and column (0-2, space-separated): ").split())

# #             if board[row][col] == " ":
# #                 board[row][col] = players[current_player]
# #                 print_board(board)

# #                 if check_winner(board, players[current_player]):
# #                     print(f"🎉 Player {players[current_player]} wins!")
# #                     break

# #                 if is_full(board):
# #                     print("It's a tie! 🤝")
# #                     break

# #                 current_player = 1 - current_player  # Switch player
# #                 time.sleep(1)
# #             else:
# #                 print("That spot is already taken. Try again!")

# #         except (ValueError, IndexError):
# #             print("Invalid input! Please enter row and column numbers between 0 and 2.")

# # # Run the game
# # if __name__ == "__main__":
# #     play_game()


# import time

# # Function to print the board
# def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)

# # Function to check for a win
# def check_winner(board, player):
#     # Check rows, columns, and diagonals
#     for row in board:
#         if all(cell == player for cell in row):
#             return True

#     for col in range(3):
#         if all(board[row][col] == player for row in range(3)):
#             return True

#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True

#     return False

# # Function to check if the board is full
# def is_full(board):
#     return all(cell != " " for row in board for cell in row)

# # Function to handle player input with validation
# def get_player_input(player):
#     while True:
#         try:
#             row, col = map(int, input(f"Player {player}, enter row and column (0-2, space-separated): ").split())
#             if 0 <= row <= 2 and 0 <= col <= 2:
#                 return row, col
#             else:
#                 print("Invalid input! Row and column must be between 0 and 2. Try again.")
#         except ValueError:
#             print("Invalid input! Please enter two integers (row and column) separated by space.")

# # Main game loop
# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     players = ["X", "O"]
#     current_player = 0

#     print("Welcome to Tic-Tac-Toe!")
#     player1_name = input("Enter name for Player X: ")
#     player2_name = input("Enter name for Player O: ")

#     print(f"\n{player1_name} (X) vs {player2_name} (O)\n")
#     print_board(board)

#     while True:
#         row, col = get_player_input(players[current_player])

#         if board[row][col] == " ":
#             board[row][col] = players[current_player]
#             print_board(board)

#             if check_winner(board, players[current_player]):
#                 print(f"🎉 {player1_name if current_player == 0 else player2_name} wins!")
#                 break

#             if is_full(board):
#                 print("It's a tie! 🤝")
#                 break

#             current_player = 1 - current_player  # Switch player
#             time.sleep(1)
#         else:
#             print("That spot is already taken. Try again!")

# # Run the game
# if __name__ == "__main__":
#     play_game()


import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(row, col):
    global game_over  # Declare game_over as global
    if board[row][col] == " " and not game_over:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            game_over = True  # Set game_over to True when someone wins
        elif is_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True  # Set game_over to True when it's a tie
        else:
            switch_player()

# Function to switch players
def switch_player():
    global current_player  # Declare current_player as global
    current_player = "O" if current_player == "X" else "X"

# Function to check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Function to check if the board is full
def is_full():
    return all(cell != " " for row in board for cell in row)

# Initialize the game
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False  # Global variable to track if the game is over

# Create the buttons for the Tic-Tac-Toe grid
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=("Arial", 24), command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Run the game
root.mainloop()
