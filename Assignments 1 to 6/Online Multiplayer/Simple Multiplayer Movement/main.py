import pygame

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Movement Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player properties
player_size = 40
player1_x, player1_y = 100, 200  # Green Player (Arrow Keys)
player2_x, player2_y = 200, 200  # Red Player (WASD Keys)
speed = 5

# Game Loop
running = True
while running:
    pygame.time.delay(30)  # Control speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # Player 1 (Arrow Keys)
    if keys[pygame.K_LEFT]:
        player1_x -= speed
    if keys[pygame.K_RIGHT]:
        player1_x += speed
    if keys[pygame.K_UP]:
        player1_y -= speed
    if keys[pygame.K_DOWN]:
        player1_y += speed
    
    # Player 2 (WASD)
    if keys[pygame.K_a]:
        player2_x -= speed
    if keys[pygame.K_d]:
        player2_x += speed
    if keys[pygame.K_w]:
        player2_y -= speed
    if keys[pygame.K_s]:
        player2_y += speed
    
    # Keep players inside window
    player1_x = max(0, min(WIDTH - player_size, player1_x))
    player1_y = max(0, min(HEIGHT - player_size, player1_y))
    player2_x = max(0, min(WIDTH - player_size, player2_x))
    player2_y = max(0, min(HEIGHT - player_size, player2_y))
    
    # Draw everything
    win.fill(BLACK)
    pygame.draw.rect(win, GREEN, (player1_x, player1_y, player_size, player_size))
    pygame.draw.rect(win, RED, (player2_x, player2_y, player_size, player_size))
    pygame.display.update()

# Quit game
pygame.quit()
