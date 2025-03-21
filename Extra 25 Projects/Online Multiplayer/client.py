import pygame
import socket
import pickle

# Setup connection to the server
HOST = "127.0.0.1"
PORT = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_pos = pickle.loads(client.recv(2048))  # Receive initial position

def draw(players):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (*players[0], 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (*players[1], 50, 50))
    pygame.display.flip()

running = True
while running:
    clock.tick(30)  # Set frame rate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos = (player_pos[0] - 5, player_pos[1])
    if keys[pygame.K_RIGHT]:
        player_pos = (player_pos[0] + 5, player_pos[1])
    if keys[pygame.K_UP]:
        player_pos = (player_pos[0], player_pos[1] - 5)
    if keys[pygame.K_DOWN]:
        player_pos = (player_pos[0], player_pos[1] + 5)

    # Send updated position to server
    client.send(pickle.dumps(player_pos))

    # Receive updated positions of both players
    try:
        players = pickle.loads(client.recv(2048))
        draw(players)
    except:
        break

pygame.quit()

