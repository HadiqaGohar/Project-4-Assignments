import pygame
import socket
import pickle

# Server IP (change to match the server's IP)
SERVER_IP = "127.0.0.1"  # Use local IP if running on LAN
PORT = 5555

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
player_pos = pickle.loads(client.recv(1024))  # Receive starting position

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))  # Background color

    # Handle events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos = (player_pos[0] - 5, player_pos[1])
    if keys[pygame.K_RIGHT]:
        player_pos = (player_pos[0] + 5, player_pos[1])
    if keys[pygame.K_UP]:
        player_pos = (player_pos[0], player_pos[1] - 5)
    if keys[pygame.K_DOWN]:
        player_pos = (player_pos[0], player_pos[1] + 5)

    # Send position update to server
    client.send(pickle.dumps(player_pos))
    players = pickle.loads(client.recv(1024))  # Receive updated positions

    # Draw players
    pygame.draw.rect(screen, (0, 0, 255), (*players[0], 50, 50))  # Player 1 (Blue)
    pygame.draw.rect(screen, (255, 0, 0), (*players[1], 50, 50))  # Player 2 (Red)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
client.close()
