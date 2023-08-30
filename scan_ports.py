import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

target_ip = "192.168.1.1" #Change to target ip 
for port in range(1, 1025):  # Scan the first 1035 ports
    scan_port(target_ip, port)
