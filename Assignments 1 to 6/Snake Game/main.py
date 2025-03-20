import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Setup display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [[100, 100]]  # Snake starting position
        self.direction = "RIGHT"
        self.growing = False

    def move(self):
        head = self.body[0][:]
        if self.direction == "UP":
            head[1] -= GRID_SIZE
        elif self.direction == "DOWN":
            head[1] += GRID_SIZE
        elif self.direction == "LEFT":
            head[0] -= GRID_SIZE
        elif self.direction == "RIGHT":
            head[0] += GRID_SIZE
        
        self.body.insert(0, head)  # Move forward
        if not self.growing:
            self.body.pop()  # Remove tail if not growing
        else:
            self.growing = False

    def grow(self):
        self.growing = True

    def check_collision(self):
        head = self.body[0]
        # Wall collision
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        # Self collision
        if head in self.body[1:]:
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE)]

    def spawn(self):
        self.position = [random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE)]

    def draw(self):
        pygame.draw.rect(win, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

# Game loop
def game():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    running = True

    while running:
        win.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Control snake direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

        # Move snake
        snake.move()

        # Check if snake eats food
        if snake.body[0] == food.position:
            snake.grow()
            food.spawn()

        # Check collision
        if snake.check_collision():
            running = False  # Game over

        # Draw snake and food
        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)  # Snake speed

    pygame.quit()

# Run game
game()
