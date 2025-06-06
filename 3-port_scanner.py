# Using Python, we're going to import the socket tool, so we can get access to the BSD socket interface and Unix systems. 

import socket

# Target domain and port range
target = "target.com"
start_port = 20
end_port = 65535
timeout = 0.5

print(f"Resolving {target}...")
try:
    ip = socket.gethostbyname(target)
    print(f"{target} resolved to {ip}")
except socket.gaierror:
    print("Error: Could not resolve domain.")
    exit(1)

print(f"\nScanning {target} ({ip}) from port {start_port} to {end_port}...\n")

# Scan the port range
for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        break
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")
