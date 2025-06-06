# Using Python, we're going to import the socket tool, so we can get access to the BSD socket interface and Unix systems. 

import socket
import ipaddress

# Define subnet and port range
subnet = "192.0.2.0/24"
start_port = 20
end_port = 65535
timeout = 0.5  # seconds

print(f"Scanning subnet: {subnet}")
print(f"Ports: {start_port}-{end_port}")
print("-" * 50)

# Convert to IP network
network = ipaddress.ip_network(subnet)

# Iterate through each host in subnet
for ip in network.hosts():
    print(f"\nScanning host {ip}...")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket()
            sock.settimeout(timeout)
            result = sock.connect_ex((str(ip), port))
            if result == 0:
                print(f"[+] {ip}:{port} is open")
            sock.close()
        except Exception as e:
            print(f"Error on {ip}:{port} -> {e}")
