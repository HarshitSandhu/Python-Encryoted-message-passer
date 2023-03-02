import socket
import sys
import os
import subprocess
from affine_cypher import *


host = socket.gethostname()
host = socket.gethostbyname(host)
port = 9999
s = socket.socket()     # TCP socket object

s.connect((host,port))

while (True):
    data = s.recv(1024) 
    key_value =  s.recv(1024) 
    message = data.decode('utf-8')
    keyC = key_value.decode('utf-8')
    keyC = int(keyC)
    #print(keyC)
    print("Recieved message:",message)
    while(True):
        key_client = int(input("Enter key:"))
        if key_client == keyC:    
            translated = decryptMessage(key_client, message)
            print("Decrypted message:",translated)
            with open('message_log.txt','a') as m:
                m.write("{},{},{}".format(key_client,translated,message))
            break
        else:
            print("invalid Key")

    # if message == 'quit':
    #     s.close()
    #     sys.exit()
    # print(message) 
s.close()