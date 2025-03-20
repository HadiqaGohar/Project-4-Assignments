import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
VELOCITY = 5
OBSTACLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodging Game")

# Player Setup
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10

# Obstacles
obstacles = []
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    pygame.time.delay(30)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move Player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= VELOCITY
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += VELOCITY
    
    # Spawn Obstacles
    if random.randint(1, 30) == 1:
        obstacles.append([random.randint(0, WIDTH - OBSTACLE_SIZE), 0])
    
    # Move Obstacles
    for obstacle in obstacles[:]:
        obstacle[1] += OBSTACLE_SPEED
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
    
    # Collision Detection
    for obstacle in obstacles:
        if (player_x < obstacle[0] < player_x + PLAYER_SIZE or player_x < obstacle[0] + OBSTACLE_SIZE < player_x + PLAYER_SIZE) and \
           (player_y < obstacle[1] + OBSTACLE_SIZE < player_y + PLAYER_SIZE):
            running = False
    
    # Draw Player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    
    # Draw Obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))
    
    # Draw Score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
