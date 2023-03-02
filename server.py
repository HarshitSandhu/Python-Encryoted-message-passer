import socket
import os 
import sys
from affine_cypher import *


def socket_create():
    global host 
    global port 
    global s
    s = socket.socket()

    host  = socket.gethostname()
    host  = socket.gethostbyname(host)
    port = 9999

def socket_bind():
    try:
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error")
        socket_bind()

def socket_accept():
    conn,address = s.accept()
    print("Connected to: ",address)
    send_message(conn)
    conn.close()

def send_message(conn):
    while (True):
        message = input('Enter message: ')
        if message=='q':
            break
        key = int(input('Enter key [2000 - 9000]: '))
        mode = input('Encrypt/Decrypt [E/D]: ')

        if mode.lower().startswith('e'):
                mode = 'encrypt'
                translated = encryptMessage(key, message)
        elif mode.lower().startswith('d'):
                mode = 'decrypt'
                translated = decryptMessage(key, message)
        # message = input()
        # if cmd == 'quit':
        #     s.close()
        #     sys.exit()
        conn.send(str.encode(translated))
        conn.send(str.encode(str(key)))
        # response = str(conn.recv(1024),'utf-8')
    

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()

