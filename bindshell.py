#!/usr/bin/python3

import sys
import socket
import threading

def tcp_connect(host, port):
    global sock ## accessible from anywhere
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port)) ## tuple
        interact()
    except Exception as err:
        print(err)
        sys.exit()
        
def recv():
    while True:
        try:
            data = sock.recv(1024)
            sys.stdout.write(data.decode('utf-8'))
            sys.stdout.flush()
        except Exception as err:
            print(err)
            sock.close()
            sys.exit()

def interact():
    th = threading.Thread(target=recv) ##recv() function??
    th.start()
    try: 
        while True:
            cmd = sys.stdin.read(1)
            sock.send(cmd.encode())
        print('Connection closed.')
        sock.close()
        sys.exit()
    except KeyboardInterrupt:
        sock.close()
        sys.exit()
        
if __name__ == '__main__':
    host = '192.168.0.56'
    port = 1524
    tcp_connect(host, port)
