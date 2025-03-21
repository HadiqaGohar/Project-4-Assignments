import pygame

pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tag Game")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Player settings
player_size = 40
player_speed = 5

# Player positions
red_x, red_y = 100, 200
green_x, green_y = 300, 200

# Chaser flag (Red starts as chaser)
is_red_chaser = True

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Controls
    keys = pygame.key.get_pressed()
    
    if is_red_chaser:
        # Red (chaser) movement (Arrow keys)
        if keys[pygame.K_LEFT]:
            red_x -= player_speed
        if keys[pygame.K_RIGHT]:
            red_x += player_speed
        if keys[pygame.K_UP]:
            red_y -= player_speed
        if keys[pygame.K_DOWN]:
            red_y += player_speed
    
    # Green (Runner) movement (WASD)
    if keys[pygame.K_a]:
        green_x -= player_speed
    if keys[pygame.K_d]:
        green_x += player_speed
    if keys[pygame.K_w]:
        green_y -= player_speed
    if keys[pygame.K_s]:
        green_y += player_speed
    
    # Collision Detection
    if abs(red_x - green_x) < player_size and abs(red_y - green_y) < player_size:
        is_red_chaser = not is_red_chaser  # Swap chaser
    
    # Draw players
    pygame.draw.rect(screen, RED if is_red_chaser else GREEN, (red_x, red_y, player_size, player_size))
    pygame.draw.rect(screen, GREEN if is_red_chaser else RED, (green_x, green_y, player_size, player_size))
    
    pygame.display.update()
    clock.tick(30)  # 30 FPS
    
pygame.quit()