#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
#import datetime
import time

tStart = time.ctime()
tStart1 = str(tStart).replace(' ','').replace(':','-')
s1 = tStart1[0:7]
s2 = tStart1[7:15]
s3 = tStart1[15:19]
tStart1 = s3+s1+" "+s2
f = open("C:/wget/0213/Recive"+tStart1+".txt","a+")
f.close()

detect_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

HOST = 'localhost'
PORT = 22232
BUFFSIZE = 4096

ADDR = (HOST,PORT)

detect_s.bind(ADDR)

# 端口号列表
flag_Port = []
i = 0
while i < 64512:
    flag_Port.append(0)
    i = i+1
print (flag_Port)
print (len(flag_Port))

while True:
    data,addr = detect_s.recvfrom(BUFFSIZE)
    print (data,addr)
    recode = str(data)+str(addr)
    f = open("C:/wget/0213/Recive"+tStart1+".txt","a+")
    f.write(recode+"\n")
    f.close()
# 将接收的端口号置1
    flag_Port[int(data)-1024] = 1
# 探测到最大端口号时回复断开连接请求
    if data==b'65535':
        print("End connecting")
        break
# 将接收的端口号回传
    else:
        detect_s.sendto(data,addr)
# 断开连接
detect_s.sendto("End connetting".encode(),addr)
detect_s.close()

# 未使用的端口号为0，可能被占用
Miss_Port = []
j = 1
while j < 64512:
    if flag_Port[j] == 0:
        Miss_Port.append(j + 1024)
    j = j+1
f = open("C:/wget/0213/Recive"+tStart1+".txt","a+")
f.write("Miss_Port:"+str(len(Miss_Port))+"\n")
f.write(str(Miss_Port))
f.close()
print (Miss_Port)
print (len(Miss_Port))