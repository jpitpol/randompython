import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"Local: {local_ip}")