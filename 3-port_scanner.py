# Using Python, we're going to import the socket tool, so we can get access to the BSD socket interface and Unix systems. The argparse tool must be imported as well in order to specify converters on a command-line.

import socket
import argparse

def open_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except socket.error:
        print("[!] Unable connect to server")
        return

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--ports", help="Port range, e.g., 20-65535")
    args = parser.parse_args()

    target = args.target
    start_port, end_port = map(int, args.ports.split("-"))

    print(f"[~] Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

if __name__ == "__main__":
    main()
