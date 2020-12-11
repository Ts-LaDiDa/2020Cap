import pandas as pd
import socket
#use pandas to read excel in same folder as .exe with format limitations
ei = pd.read_excel('orders.xlsx', sheet_name='Order')
#declaration of shortform variables, BM= Bloody Mary, WR= White Russian etc
output=""
BM = ""
WR = ""
AM = ""
SD = ""
JC = ""

HOST = '142.55.148.138'
PORT = 55555
dc_con = 'dis'



def Output_Form(rawmsg):
    if len(rawmsg)<19 :
         formated = rawmsg + ' '*(19-len(rawmsg))
    else:
        formated = rawmsg
        
    return formated.encode('utf-8')

def excelread():
    #reads maximum row and columns, legacy from testing, may be useful later
    col = ei.shape[1]
    row = ei.shape[0]
    #Reads each drinks name and ID via cell location. Note: First row in excel is null
    BM = str(ei.iat[0,0]) + "!" + str(ei.iat[1,0])+","
    WR = str(ei.iat[0,1]) + "!" + str(ei.iat[1,1])+","
    AM = str(ei.iat[0,2]) + "!" + str(ei.iat[1,2])+","
    SD = str(ei.iat[0,3]) + "!" + str(ei.iat[1,3])+","
    JC = str(ei.iat[0,4]) + "!" + str(ei.iat[1,4])#+","
    #Testing output to make sure it read properly
    output=BM+WR+AM+SD+JC
    #print(output)
    return output

def to_ls(s_var):
    s_arr = s_var.split(',')
    i = len(s_arr)
    
    for e in range(i):
        s_arr[e] =s_arr[e].split('!')
        
    return s_arr
    

def data_server():
    
    lpb =True
    
    preSend_s = excelread()
    PreSend_arr = to_ls(preSend_s)
    
    index = len(PreSend_arr)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    
    conn, addr = s.accept()
    
    #while conn:
    print(f'[CONN]CLIENT {addr[0]} IS CONNECTED')
    #recv_msg = conn.recv(4096)
    #print(recv_msg.decode('utf-8'))
    
    while lpb:
         recv_msg = conn.recv(64)
         if not recv_msg:
             break
         print(recv_msg.decode('utf-8'))
         for i in range(5):
             print(i)
             if i != 0:
                 next_msg = conn.recv(256).decode('utf-8')
                 print(f'client msg: {next_msg}')
    
             send_name = PreSend_arr[i][0]
    
             send_num = PreSend_arr[i][1]
             print(f'Confirm {send_num} of {send_name}')
    
             send_name = Output_Form(send_name)
             conn.send(send_name)
    
             conn.send(send_num.encode('utf-8'))
             print('order confirmed, please wait for the next round')
    
         conn.send(dc_con.encode('utf-8'))
         lpb = False
    conn.close()
    print('data transfer end')
            
if __name__ == '__main__':
    data_server()