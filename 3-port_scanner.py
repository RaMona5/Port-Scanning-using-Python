# Using Python, we're going to import the socket tool, so we can get access to the BSD socket interface and Unix systems. 

import socket

target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"Scanning {target} from port {start_port} to {end_port}...")

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
