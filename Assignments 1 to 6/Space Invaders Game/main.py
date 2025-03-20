import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_width = 64
player_height = 64
player_speed = 5
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_img = pygame.image.load("player.png")

# Bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Alien settings
alien_width = 64
alien_height = 64
alien_speed = 3
aliens = []

# Font settings
font = pygame.font.SysFont("Arial", 30)

# Game variables
score = 0
lives = 3
game_over = False

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - player_width:
            self.rect.x += player_speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.append(bullet)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y

    def update(self):
        self.rect.y -= bullet_speed
        if self.rect.bottom < 0:
            bullets.remove(self)

# Alien class
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((alien_width, alien_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += alien_speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - alien_width)
            self.rect.y = random.randint(-100, -40)

# Set up sprite groups
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()

# Create player instance
player = Player()
player_group.add(player)

# Create aliens
for i in range(6):
    for j in range(5):
        alien = Alien(i * (alien_width + 10) + 50, j * (alien_height + 10) + 50)
        alien_group.add(alien)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot()

    # Update game objects
    keys = pygame.key.get_pressed()
    player_group.update(keys)
    for bullet in bullets:
        bullet.update()
    for alien in alien_group:
        alien.update()

    # Collision detection
    for bullet in bullets:
        for alien in alien_group:
            if bullet.rect.colliderect(alien.rect):
                alien_group.remove(alien)
                bullets.remove(bullet)
                score += 10
                break

    # Check for player-alien collisions
    for alien in alien_group:
        if alien.rect.colliderect(player.rect):
            lives -= 1
            alien.rect.x = random.randint(0, SCREEN_WIDTH - alien_width)
            alien.rect.y = random.randint(-100, -40)
            if lives == 0:
                game_over = True

    # Draw everything
    player_group.draw(screen)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    alien_group.draw(screen)

    # Display score and lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))

    # Game over screen
    if game_over:
        game_over_text = font.render("GAME OVER!", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
