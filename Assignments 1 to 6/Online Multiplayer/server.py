import socket
import pickle
import threading

# Server setup
HOST = "127.0.0.1"  # Localhost
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # Allow two players

print("Waiting for connections...")

players = [(50, 50), (200, 200)]  # Initial positions for two players

def handle_client(conn, player_id):
    global players
    conn.send(pickle.dumps(players[player_id]))  # Send initial position

    while True:
        try:
            data = pickle.loads(conn.recv(2048))  # Receive new position
            if not data:
                break
            players[player_id] = data  # Update position
            conn.send(pickle.dumps(players))  # Send updated positions
        except:
            break

    print(f"Player {player_id} disconnected")
    conn.close()

# Accept connections from clients
player_id = 0
while player_id < 2:
    conn, addr = server.accept()
    print(f"Connected to: {addr}")
    threading.Thread(target=handle_client, args=(conn, player_id)).start()
    player_id += 1
