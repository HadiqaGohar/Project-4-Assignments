import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
COLUMNS = WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tetromino Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 255, 255)]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0  # Starting position at the top

    def move(self, dx, dy, grid):
        if self.valid_position(self.x + dx, self.y + dy, grid):
            self.x += dx
            self.y += dy
            return True
        return False

    def rotate(self, grid):
        rotated_shape = [list(row) for row in zip(*self.shape[::-1])]
        if self.valid_position(self.x, self.y, grid, rotated_shape):
            self.shape = rotated_shape

    def valid_position(self, x, y, grid, shape=None):
        if shape is None:
            shape = self.shape
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    new_x = x + col
                    new_y = y + row
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return False
                    if new_y >= 0 and grid[new_y][new_x] != BLACK:
                        return False
        return True

def create_grid(locked_positions):
    grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

def clear_rows(grid, locked_positions):
    full_rows = []
    for row in range(ROWS):
        if all(grid[row][col] != BLACK for col in range(COLUMNS)):
            full_rows.append(row)

    if full_rows:
        for row in full_rows:
            for col in range(COLUMNS):
                del locked_positions[(col, row)]

        for row in reversed(range(ROWS)):
            for col in range(COLUMNS):
                if (col, row) in locked_positions:
                    new_row = row + len([r for r in full_rows if r > row])
                    locked_positions[(col, new_row)] = locked_positions.pop((col, row))

def draw_grid(screen, grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def draw_tetromino(screen, tetromino):
    for row in range(len(tetromino.shape)):
        for col in range(len(tetromino.shape[row])):
            if tetromino.shape[row][col]:
                pygame.draw.rect(screen, tetromino.color, 
                                 ((tetromino.x + col) * GRID_SIZE, (tetromino.y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris Game")
    clock = pygame.time.Clock()
    running = True
    locked_positions = {}
    grid = create_grid(locked_positions)

    # First Tetromino
    falling_tetromino = Tetromino()

    # **Fix Added Here**
    if not falling_tetromino.valid_position(falling_tetromino.x, falling_tetromino.y, grid):
        print("Game Over!")
        pygame.quit()
        return

    while running:
        grid = create_grid(locked_positions)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    falling_tetromino.move(-1, 0, grid)
                if event.key == pygame.K_RIGHT:
                    falling_tetromino.move(1, 0, grid)
                if event.key == pygame.K_DOWN:
                    falling_tetromino.move(0, 1, grid)
                if event.key == pygame.K_UP:
                    falling_tetromino.rotate(grid)

        # Move piece down every frame
        if not falling_tetromino.move(0, 1, grid):
            for row in range(len(falling_tetromino.shape)):
                for col in range(len(falling_tetromino.shape[row])):
                    if falling_tetromino.shape[row][col]:
                        locked_positions[(falling_tetromino.x + col, falling_tetromino.y + row)] = falling_tetromino.color

            falling_tetromino = Tetromino()

            # **Fix:** Prevent Instant Game Over
            if not falling_tetromino.valid_position(falling_tetromino.x, falling_tetromino.y, grid):
                print("Game Over!")
                running = False

        clear_rows(grid, locked_positions)
        draw_grid(screen, grid)
        draw_tetromino(screen, falling_tetromino)
        pygame.display.update()
        clock.tick(1)

    pygame.quit()

if __name__ == "__main__":
    main()
