import socket
from IPy import IP


print('''
 
  ____            _     _____ _           _           
 |  _ \ ___  _ __| |_  |  ___(_)_ __   __| | ___ _ __ 
 | |_) / _ \| '__| __| | |_  | | '_ \ / _` |/ _ \ '__|
 |  __/ (_) | |  | |_  |  _| | | | | | (_| |  __/ |   
 |_|   \___/|_|   \__| |_|   |_|_| |_|\__,_|\___|_|   
                                                     
==================== Created By vardhan ====================
''')


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[ Scanning target ] ' + str(target) + "\n")
    for port in range(1, 100):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(f"Open port {port} : {banner.decode()} ")
        except:
            print(f"Port {port} is open ")
    except:
        pass


targets = input(
    "Enter the target/s to scan (split multiple targets with comma) : ")

if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
