# import math

# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)

# def check_winner(board):
#     for row in board:
#         if row.count(row[0]) == 3 and row[0] != " ":
#             return row[0]
    
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
#             return board[0][col]
    
#     if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
#         return board[0][2]
    
#     return None

# def is_full(board):
#     return all(cell != " " for row in board for cell in row)

# def minimax(board, depth, is_maximizing):
#     winner = check_winner(board)
#     if winner == "O":
#         return 1
#     if winner == "X":
#         return -1
#     if is_full(board):
#         return 0
    
#     if is_maximizing:
#         best_score = -math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == " ":
#                     board[i][j] = "O"
#                     score = minimax(board, depth + 1, False)
#                     board[i][j] = " "
#                     best_score = max(score, best_score)
#         return best_score
#     else:
#         best_score = math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == " ":
#                     board[i][j] = "X"
#                     score = minimax(board, depth + 1, True)
#                     board[i][j] = " "
#                     best_score = min(score, best_score)
#         return best_score

# def best_move(board):
#     best_score = -math.inf
#     move = None
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == " ":
#                 board[i][j] = "O"
#                 score = minimax(board, 0, False)
#                 board[i][j] = " "
#                 if score > best_score:
#                     best_score = score
#                     move = (i, j)
#     return move

# def main():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     print("Tic-Tac-Toe AI - You are X, AI is O")
#     print_board(board)
    
#     while True:
#         row, col = map(int, input("Enter row and column (0-2): ").split())
#         if board[row][col] == " ":
#             board[row][col] = "X"
#         else:
#             print("Invalid move, try again!")
#             continue
        
#         if check_winner(board):
#             print_board(board)
#             print("You win!")
#             break
#         if is_full(board):
#             print_board(board)
#             print("It's a tie!")
#             break
        
#         print("AI's turn...")
#         ai_move = best_move(board)
#         board[ai_move[0]][ai_move[1]] = "O"
        
#         print_board(board)
        
#         if check_winner(board):
#             print("AI wins!")
#             break
#         if is_full(board):
#             print("It's a tie!")
#             break

# if __name__ == "__main__":
#     main()



import tkinter as tk
from tkinter import messagebox
import math
import time

# Function to print the board (for console purposes)
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if there's a winner
def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

# Check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm for AI decision making
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Function to get the best AI move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to update the board on the GUI
def update_board(board, buttons):
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

# Function to handle player move
def player_move(row, col, board, buttons):
    if board[row][col] == " ":
        board[row][col] = "X"
        update_board(board, buttons)
        return True
    else:
        return False

# Function to handle AI move with a twinkle effect
def ai_move(board, buttons):
    move = best_move(board)
    time.sleep(0.5)  # Pause for twinkle effect
    row, col = move
    board[row][col] = "O"
    update_board(board, buttons)
    time.sleep(0.5)  # Pause for the move to settle visually

# Function to check the game status
def check_game_status(board, root):
    winner = check_winner(board)
    if winner == "X":
        messagebox.showinfo("Game Over", "You win!")
        root.quit()
    elif winner == "O":
        messagebox.showinfo("Game Over", "AI wins!")
        root.quit()
    elif is_full(board):
        messagebox.showinfo("Game Over", "It's a tie!")
        root.quit()

# Create the main game window
def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe - AI vs You")
    
    # Initialize game variables
    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    
    # Create buttons for the game grid
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=("Arial", 24),
                                      command=lambda i=i, j=j: on_button_click(i, j, board, buttons, root))
            buttons[i][j].grid(row=i, column=j)
    
    # Start the game
    root.mainloop()

# Function to handle button click (Player's move)
def on_button_click(row, col, board, buttons, root):
    if player_move(row, col, board, buttons):
        check_game_status(board, root)
        ai_move(board, buttons)
        check_game_status(board, root)

if __name__ == "__main__":
    main()
