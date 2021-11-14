import socket
import threading
import sys


scanningMode = False
hostDown = True

def scan_port(ip, port, tm):
    global hostDown
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(tm)
    try:
        connect = sock.connect((ip, port))
        print("Port " + str(port) + " is opened.")
        if hostDown:
            hostDown = False
        sock.close()
    except:
        pass
if "scan" in sys.argv:
    scanningMode = True
if"-ip" in sys.argv:
    indexofip=sys.argv.index("-ip")
    ip=sys.argv[indexofip + 1]
if "-p" in sys.argv:
    indexofp = sys.argv.index("-p")
    ports = int(sys.argv[indexofp + 1])
if "-t" in sys.argv:
    indexoftimeout = sys.argv.index("-t")
    timeout = float(sys.argv[indexoftimeout + 1])
if "--help" in sys.argv:
    print("scan if you want to scan ports")
    print("--help show this")
    print("-ip *ip* to specify host ip")
    print("-p *ports count* to specify how many ports will be scanned")
    print("-t *timeout* to specify timeout between breaking of connection")
    print("example: internetTool.py scan -ip 192.168.0.1 -p 1024 -t 0.5")
    exit()
if len(sys.argv) < 2:
    print("--help for help with syntax")


if scanningMode:
    for i in range(ports):
        th = threading.Thread(target=scan_port, args=(ip,i, timeout))
        th.start()
    if hostDown:
        print("Host seems down")