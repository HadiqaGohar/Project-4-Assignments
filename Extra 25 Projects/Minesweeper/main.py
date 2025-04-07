# # # # import random

# # # # class Minesweeper:
# # # #     def __init__(self, size=5, bombs=3):
# # # #         self.size = size
# # # #         self.bombs = bombs
# # # #         self.board = [[' ' for _ in range(size)] for _ in range(size)]
# # # #         self.bomb_positions = set()
# # # #         self.revealed = set()
# # # #         self._place_bombs()

# # # #     def _place_bombs(self):
# # # #         while len(self.bomb_positions) < self.bombs:
# # # #             r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
# # # #             self.bomb_positions.add((r, c))

# # # #     def _count_adjacent_bombs(self, r, c):
# # # #         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# # # #         count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
# # # #         return count

# # # #     def reveal(self, r, c):
# # # #         if (r, c) in self.bomb_positions:
# # # #             print("💣 You hit a bomb! Game Over!")
# # # #             return False
        
# # # #         if (r, c) in self.revealed:
# # # #             return True

# # # #         self.revealed.add((r, c))
# # # #         bomb_count = self._count_adjacent_bombs(r, c)
# # # #         self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

# # # #         if bomb_count == 0:
# # # #             for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
# # # #                 nr, nc = r + dr, c + dc
# # # #                 if 0 <= nr < self.size and 0 <= nc < self.size:
# # # #                     self.reveal(nr, nc)

# # # #         return True

# # # #     def display(self):
# # # #         for row in self.board:
# # # #             print(' '.join(row))
# # # #         print()

# # # #     def play(self):
# # # #         while True:
# # # #             self.display()
# # # #             try:
# # # #                 r, c = map(int, input("Enter row and column (e.g., 1 2): ").split())
# # # #                 if not (0 <= r < self.size and 0 <= c < self.size):
# # # #                     print("Invalid input, try again.")
# # # #                     continue
# # # #                 if not self.reveal(r, c):
# # # #                     break
# # # #                 if len(self.revealed) == (self.size ** 2 - self.bombs):
# # # #                     print("🎉 Congratulations! You cleared the board!")
# # # #                     break
# # # #             except ValueError:
# # # #                 print("Invalid input, enter two numbers.")

# # # # # Start Game
# # # # game = Minesweeper(size=5, bombs=3)
# # # # game.play()

# # # # -----------------------------------------------

# # # import random
# # # import tkinter as tk
# # # from tkinter import messagebox

# # # class Minesweeper:
# # #     def __init__(self, size=5, bombs=3):
# # #         self.size = size
# # #         self.bombs = bombs
# # #         self.board = [[' ' for _ in range(size)] for _ in range(size)]
# # #         self.bomb_positions = set()
# # #         self.revealed = set()
# # #         self._place_bombs()

# # #         self.root = tk.Tk()
# # #         self.root.title("Minesweeper Game")
# # #         self.buttons = {}

# # #         # Creating the game grid with buttons
# # #         for row in range(self.size):
# # #             for col in range(self.size):
# # #                 button = tk.Button(self.root, text=" ", width=4, height=2, command=lambda r=row, c=col: self.reveal(r, c))
# # #                 button.grid(row=row, column=col)
# # #                 self.buttons[(row, col)] = button

# # #     def _place_bombs(self):
# # #         while len(self.bomb_positions) < self.bombs:
# # #             r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
# # #             self.bomb_positions.add((r, c))

# # #     def _count_adjacent_bombs(self, r, c):
# # #         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# # #         count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
# # #         return count

# # #     def reveal(self, r, c):
# # #         if (r, c) in self.bomb_positions:
# # #             messagebox.showinfo("Game Over", "💣 You hit a bomb! Game Over!")
# # #             self.root.quit()
# # #             return

# # #         if (r, c) in self.revealed:
# # #             return

# # #         self.revealed.add((r, c))
# # #         bomb_count = self._count_adjacent_bombs(r, c)
# # #         self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

# # #         button = self.buttons[(r, c)]
# # #         button.config(text=self.board[r][c], state="disabled", relief="sunken", bg="lightblue")

# # #         if bomb_count == 0:
# # #             for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
# # #                 nr, nc = r + dr, c + dc
# # #                 if 0 <= nr < self.size and 0 <= nc < self.size:
# # #                     self.reveal(nr, nc)

# # #         if len(self.revealed) == (self.size ** 2 - self.bombs):
# # #             messagebox.showinfo("Congratulations", "🎉 You cleared the board!")
# # #             self.root.quit()

# # #     def play(self):
# # #         self.root.mainloop()

# # # # Start the game
# # # game = Minesweeper(size=5, bombs=3)
# # # game.play()

# # # # ----------------------------------

# # import random
# # import tkinter as tk
# # from tkinter import messagebox
# # import time

# # class Minesweeper:
# #     def __init__(self, size=5, bombs=3):
# #         self.size = size
# #         self.bombs = bombs
# #         self.board = [[' ' for _ in range(size)] for _ in range(size)]
# #         self.bomb_positions = set()
# #         self.revealed = set()
# #         self._place_bombs()
# #         self.start_time = None

# #         self.root = tk.Tk()
# #         self.root.title("Minesweeper Game")
        
# #         # Timer label
# #         self.timer_label = tk.Label(self.root, text="Time: 0", font=("Arial", 14))
# #         self.timer_label.grid(row=0, column=0, columnspan=self.size, pady=5)

# #         # Difficulty Level Buttons
# #         self.easy_button = tk.Button(self.root, text="Easy (5x5)", command=lambda: self.new_game(5, 3))
# #         self.easy_button.grid(row=self.size+1, column=0)
        
# #         self.medium_button = tk.Button(self.root, text="Medium (8x8)", command=lambda: self.new_game(8, 10))
# #         self.medium_button.grid(row=self.size+1, column=1)
        
# #         self.hard_button = tk.Button(self.root, text="Hard (10x10)", command=lambda: self.new_game(10, 20))
# #         self.hard_button.grid(row=self.size+1, column=2)
        
# #         self.buttons = {}

# #         self._create_grid()

# #     def new_game(self, size, bombs):
# #         self.size = size
# #         self.bombs = bombs
# #         self.board = [[' ' for _ in range(size)] for _ in range(size)]
# #         self.bomb_positions = set()
# #         self.revealed = set()
# #         self._place_bombs()
        
# #         # Reset timer
# #         self.start_time = time.time()
# #         self.timer_label.config(text="Time: 0")
        
# #         # Update button grid
# #         self._create_grid()

# #     def _place_bombs(self):
# #         while len(self.bomb_positions) < self.bombs:
# #             r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
# #             self.bomb_positions.add((r, c))

# #     def _count_adjacent_bombs(self, r, c):
# #         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# #         count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
# #         return count

# #     def reveal(self, r, c):
# #         if self.start_time is None:
# #             self.start_time = time.time()

# #         if (r, c) in self.bomb_positions:
# #             messagebox.showinfo("Game Over", "💣 You hit a bomb! Game Over!")
# #             self.root.quit()
# #             return

# #         if (r, c) in self.revealed:
# #             return

# #         self.revealed.add((r, c))
# #         bomb_count = self._count_adjacent_bombs(r, c)
# #         self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

# #         button = self.buttons[(r, c)]
# #         button.config(text=self.board[r][c], state="disabled", relief="sunken", bg=self._get_button_color(bomb_count))

# #         if bomb_count == 0:
# #             for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
# #                 nr, nc = r + dr, c + dc
# #                 if 0 <= nr < self.size and 0 <= nc < self.size:
# #                     self.reveal(nr, nc)

# #         if len(self.revealed) == (self.size ** 2 - self.bombs):
# #             end_time = time.time() - self.start_time
# #             messagebox.showinfo("Congratulations", f"🎉 You cleared the board in {int(end_time)} seconds!")
# #             self.root.quit()

# #     def _get_button_color(self, bomb_count):
# #         color_map = {
# #             0: "lightgray",
# #             1: "lightblue",
# #             2: "lightgreen",
# #             3: "yellow",
# #             4: "orange",
# #             5: "red",
# #             6: "darkred",
# #             7: "purple",
# #             8: "pink"
# #         }
# #         return color_map.get(bomb_count, "white")

# #     def _create_grid(self):
# #         for row in range(self.size):
# #             for col in range(self.size):
# #                 button = tk.Button(self.root, text=" ", width=4, height=2, command=lambda r=row, c=col: self.reveal(r, c))
# #                 button.grid(row=row+1, column=col)
# #                 self.buttons[(row, col)] = button

# #         # Update the timer every second
# #         self._update_timer()

# #     def _update_timer(self):
# #         if self.start_time is not None:
# #             elapsed_time = int(time.time() - self.start_time)
# #             self.timer_label.config(text=f"Time: {elapsed_time}")
# #         self.root.after(1000, self._update_timer)

# #     def play(self):
# #         self.root.mainloop()

# # # Start the game with default Easy mode
# # game = Minesweeper(size=5, bombs=3)
# # game.play()


# # # # # ----------------------------------

# import random
# import tkinter as tk
# from tkinter import messagebox
# import time

# class Minesweeper:
#     def __init__(self, size=5, bombs=3):
#         self.size = size
#         self.bombs = bombs
#         self.board = [[' ' for _ in range(size)] for _ in range(size)]
#         self.bomb_positions = set()
#         self.revealed = set()
#         self._place_bombs()
        
#         self.root = tk.Tk()
#         self.root.title("Minesweeper Game")
#         self.buttons = {}
#         self.start_time = None
        
#         # Timer Label
#         self.timer_label = tk.Label(self.root, text="Time: 0", font=('Arial', 14))
#         self.timer_label.grid(row=self.size, columnspan=self.size, pady=10)
        
#         # Creating the game grid with buttons
#         for row in range(self.size):
#             for col in range(self.size):
#                 button = tk.Button(self.root, text=" ", width=4, height=2, command=lambda r=row, c=col: self.reveal(r, c))
#                 button.grid(row=row, column=col)
#                 self.buttons[(row, col)] = button
        
#         # Reset Button
#         self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
#         self.reset_button.grid(row=self.size + 1, columnspan=self.size, pady=10)

#     def _place_bombs(self):
#         while len(self.bomb_positions) < self.bombs:
#             r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
#             self.bomb_positions.add((r, c))

#     def _count_adjacent_bombs(self, r, c):
#         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#         count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
#         return count

#     def reveal(self, r, c):
#         if not self.start_time:
#             self.start_time = time.time()

#         if (r, c) in self.bomb_positions:
#             messagebox.showinfo("Game Over", "💣 You hit a bomb! Game Over!")
#             self.root.quit()
#             return

#         if (r, c) in self.revealed:
#             return

#         self.revealed.add((r, c))
#         bomb_count = self._count_adjacent_bombs(r, c)
#         self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

#         button = self.buttons[(r, c)]
#         button.config(text=self.board[r][c], state="disabled", relief="sunken", bg="lightblue")

#         if bomb_count == 0:
#             for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < self.size and 0 <= nc < self.size:
#                     self.reveal(nr, nc)

#         if len(self.revealed) == (self.size ** 2 - self.bombs):
#             elapsed_time = int(time.time() - self.start_time)
#             messagebox.showinfo("Congratulations", f"🎉 You cleared the board in {elapsed_time} seconds!")
#             self.root.quit()

#         self.update_timer()

#     def update_timer(self):
#         if self.start_time:
#             elapsed_time = int(time.time() - self.start_time)
#             self.timer_label.config(text=f"Time: {elapsed_time}")
#         self.root.after(1000, self.update_timer)

#     def reset_game(self):
#         self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
#         self.bomb_positions = set()
#         self.revealed = set()
#         self._place_bombs()
#         self.start_time = None
#         self.timer_label.config(text="Time: 0")

#         for button in self.buttons.values():
#             button.config(text=" ", state="normal", relief="raised", bg="lightgrey")

#     def play(self):
#         self.root.mainloop()

# # Start the game
# game = Minesweeper(size=5, bombs=3)
# game.play()


# # --------------------------

import random
import tkinter as tk
from tkinter import messagebox
import time

class Minesweeper:
    def __init__(self, size=5, bombs=3):
        self.size = size
        self.bombs = bombs
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.bomb_positions = set()
        self.revealed = set()
        self.flagged = set()
        self.start_time = None
        
        # Initializing Tkinter window
        self.root = tk.Tk()
        self.root.title("Minesweeper Game")
        
        self.buttons = {}
        self.timer_label = tk.Label(self.root, text="Time: 0", font=('Arial', 14))
        self.timer_label.grid(row=self.size, columnspan=self.size, pady=10)
        
        # Difficulty Selection Dropdown
        self.difficulty_var = tk.StringVar(self.root)
        self.difficulty_var.set("Easy")
        difficulty_menu = tk.OptionMenu(self.root, self.difficulty_var, "Easy", "Medium", "Hard", command=self.change_difficulty)
        difficulty_menu.grid(row=self.size + 1, columnspan=self.size, pady=5)
        
        # Creating game grid with buttons
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.root, text=" ", width=4, height=2, command=lambda r=row, c=col: self.reveal(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button
        
        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=self.size + 2, columnspan=self.size, pady=10)
        
        self.play_sound('start')

    def play_sound(self, action):
        sounds = {
            'start': 'start_sound.mp3',
            'click': 'click_sound.mp3',
            'bomb': 'bomb_sound.mp3',
            'win': 'win_sound.mp3',
            'lose': 'lose_sound.mp3',
        }
        if action in sounds:
            # Replace this with an actual sound playing function
            print(f"Playing sound: {sounds[action]}")

    def _place_bombs(self):
        while len(self.bomb_positions) < self.bombs:
            r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.bomb_positions.add((r, c))

    def _count_adjacent_bombs(self, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
        return count

    def reveal(self, r, c):
        if not self.start_time:
            self.start_time = time.time()

        if (r, c) in self.flagged:
            return

        if (r, c) in self.bomb_positions:
            self.play_sound('bomb')
            self.end_game("Game Over", "💣 You hit a bomb!")
            return

        if (r, c) in self.revealed:
            return

        self.revealed.add((r, c))
        bomb_count = self._count_adjacent_bombs(r, c)
        self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

        button = self.buttons[(r, c)]
        button.config(text=self.board[r][c], state="disabled", relief="sunken", bg="lightblue")

        if bomb_count == 0:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    self.reveal(nr, nc)

        if len(self.revealed) == (self.size ** 2 - self.bombs):
            self.play_sound('win')
            elapsed_time = int(time.time() - self.start_time)
            self.end_game("Congratulations!", f"🎉 You cleared the board in {elapsed_time} seconds!")

        self.update_timer()

    def update_timer(self):
        if self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed_time}")
        self.root.after(1000, self.update_timer)

    def end_game(self, title, message):
        messagebox.showinfo(title, message)
        self.root.quit()

    def reset_game(self):
        self.size, self.bombs = self._get_difficulty_params()
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.bomb_positions = set()
        self.revealed = set()
        self.flagged = set()
        self._place_bombs()
        self.start_time = None
        self.timer_label.config(text="Time: 0")

        for button in self.buttons.values():
            button.config(text=" ", state="normal", relief="raised", bg="lightgrey")
        self.play_sound('start')

    def change_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.size = 5
            self.bombs = 5
        elif difficulty == "Medium":
            self.size = 8
            self.bombs = 12
        else:
            self.size = 10
            self.bombs = 20
        self.reset_game()

    def _get_difficulty_params(self):
        if self.difficulty_var.get() == "Easy":
            return 5, 5
        elif self.difficulty_var.get() == "Medium":
            return 8, 12
        else:
            return 10, 20

    def play(self):
        self.root.mainloop()

# Start the game
game = Minesweeper(size=5, bombs=3)
game.play()
