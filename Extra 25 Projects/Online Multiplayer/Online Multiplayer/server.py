import socket
import pickle

# Server settings
HOST = "0.0.0.0"  # Allows connections from any device
PORT = 5555

# Start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # Accept up to 2 players
print("Server started. Waiting for players...")

# Initial player positions
players = [(100, 100), (300, 100)]

def handle_client(conn, player_id):
    global players
    conn.send(pickle.dumps(players[player_id]))  # Send initial position

    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            if not data:
                break
            players[player_id] = data  # Update player position
            conn.send(pickle.dumps(players))  # Send updated positions
        except:
            break

    print(f"Player {player_id+1} disconnected")
    conn.close()

# Accept connections
for i in range(2):
    conn, addr = server.accept()
    print(f"Player {i+1} connected from {addr}")
    handle_client(conn, i)
