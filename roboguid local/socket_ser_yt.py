# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:39:00 2020

@author: tuya
"""
import socket

HOST = '142.55.148.138'
PORT = 55555
dc_con = 'disconnect'

def Output_Form(rawmsg):
    if len(rawmsg)<10 :
         formated = rawmsg + ' '*(10-len(rawmsg))
    else:
        formated = rawmsg
        
    return formated.encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
#conn.send(str('Welcome... \n').encod.e('utf-8'))
while conn:
    print(f'[CONN]CLIENT {addr[0]} IS CONNECTED')
    #f = open('FANUC_otpt.txt','a')
    while True:
        recv_msg = conn.recv(4096)
        if not recv_msg:
            break
        
        print(recv_msg.decode('utf-8'))
        send_name = input('Please say something: ')
        print(f'the sent msg is: {send_name}')
        
        #print(f'Confirm {send_num} of {send_name}')
        
        if send_name != dc_con:
            send_name = Output_Form(send_name)
            conn.send(send_name)
        else:
            break
        
        send_num = input('how many drink you soule like: ')
        conn.send(send_num.encode('utf-8'))
        
        print('order confirmed, please wait for the next round')
       
        
conn.close()

