import socket
import argparse
from datetime import datetime

def tcp_scan(ip, port, banner=False):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] TCP Port {port} is open")
            if banner:
                try:
                    s.send(b"Hello\r\n")
                    data = s.recv(1024)
                    print(f"    Banner: {data.decode().strip()}")
                except:
                    print("    Banner: [Could not grab]")
        s.close()
    except Exception as e:
        print(f"Error on TCP port {port}: {e}")

def udp_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        s.sendto(b"Hello", (ip, port))
        s.recvfrom(1024)
        print(f"[+] UDP Port {port} is open")
    except socket.timeout:
        print(f"[-] UDP Port {port} is closed or filtered")
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Minimal Port Scanner")
    parser.add_argument("--ip", required=True, help="Target IP")
    parser.add_argument("--start-port", type=int, required=True)
    parser.add_argument("--end-port", type=int, required=True)
    parser.add_argument("--tcp", action="store_true")
    parser.add_argument("--udp", action="store_true")
    parser.add_argument("--banner", action="store_true")

    args = parser.parse_args()
    print(f"Scanning {args.ip} from port {args.start_port} to {args.end_port}")
    print("Started at:", datetime.now())

    for port in range(args.start_port, args.end_port + 1):
        if args.tcp:
            tcp_scan(args.ip, port, args.banner)
        if args.udp:
            udp_scan(args.ip, port)

    print("Scan completed at:", datetime.now())

if __name__ == "__main__":
    main()
