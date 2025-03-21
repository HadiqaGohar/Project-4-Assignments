import random

class Minesweeper:
    def __init__(self, size=5, bombs=3):
        self.size = size
        self.bombs = bombs
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.bomb_positions = set()
        self.revealed = set()
        self._place_bombs()

    def _place_bombs(self):
        while len(self.bomb_positions) < self.bombs:
            r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.bomb_positions.add((r, c))

    def _count_adjacent_bombs(self, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = sum((r+dr, c+dc) in self.bomb_positions for dr, dc in directions)
        return count

    def reveal(self, r, c):
        if (r, c) in self.bomb_positions:
            print("💣 You hit a bomb! Game Over!")
            return False
        
        if (r, c) in self.revealed:
            return True

        self.revealed.add((r, c))
        bomb_count = self._count_adjacent_bombs(r, c)
        self.board[r][c] = str(bomb_count) if bomb_count > 0 else '0'

        if bomb_count == 0:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    self.reveal(nr, nc)

        return True

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def play(self):
        while True:
            self.display()
            try:
                r, c = map(int, input("Enter row and column (e.g., 1 2): ").split())
                if not (0 <= r < self.size and 0 <= c < self.size):
                    print("Invalid input, try again.")
                    continue
                if not self.reveal(r, c):
                    break
                if len(self.revealed) == (self.size ** 2 - self.bombs):
                    print("🎉 Congratulations! You cleared the board!")
                    break
            except ValueError:
                print("Invalid input, enter two numbers.")

# Start Game
game = Minesweeper(size=5, bombs=3)
game.play()
