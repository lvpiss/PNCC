#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import time
import random
import socket
import string

#起始时间
tStart = time.time()

#隐蔽信息
f = open("C:/Users/lee/Documents/code/udp/covert.txt","r")
str = f.read()
print(str)
f.close()

#随机获取源端口号
r1 = random.randint(1025,65535)
r2 = random.randint(1025,65535)
r3 = random.randint(1025,65535)
r4 = random.randint(1025,65535)
print(r1,r2,r3,r4)

#字典
listrand = [r1,r2,r3,r4]
listabd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = 0

#全排列编码
dictabd = {}
for l1 in listrand:
	for l2 in listrand:
		for l3 in listrand:
			for l4 in listrand:
				if x < 26:
					dictabd[listabd[x]] = [l1,l2,l3,l4]
				x = x + 1
dictabd[' '] = [r4,r4,r4,r4]
l = len(str)
print(l)
print(dictabd)
i= 0 
listport = []
while i < l:
	listportadd = [dictabd[str[i]][0]] + [dictabd[str[i]][1]] + [dictabd[str[i]][2]] + [dictabd[str[i]][3]]
	listport = listport + listportadd
	i = i + 1

#源端口发送队列
print(len(listport))
print(listport)

timeout = 1
j = 0

#初始化通信
while j < 4:
	detect_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	socket.setdefaulttimeout(timeout)
	des_HOST = 'localhost'
	loc_HOST = 'localhost'
	PORT = 22225
	BUFFSIZE = 4096
	ADDR = (des_HOST,PORT)
	sta_PORT = listrand[j]
	try:
	    print(sta_PORT)
	    detect_s.bind((loc_HOST,sta_PORT))
	    detect_s.sendto('test'.encode(),ADDR)
	    data,ADDR = detect_s.recvfrom(BUFFSIZE)
	    print (data)
	except OSError:
	    break
	except OverflowError:
	    break
	finally:
	    j = j+1
	    pass

j = 0
#传送隐蔽信息
while j < len(listport):
	detect_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	socket.setdefaulttimeout(timeout)
	des_HOST = 'localhost'
	loc_HOST = 'localhost'
	PORT = 22225
	BUFFSIZE = 4096
	ADDR = (des_HOST,PORT)
	sta_PORT = listport[j]
	try:
	    print(sta_PORT)
	    detect_s.bind((loc_HOST,sta_PORT))
	    detect_s.sendto('test'.encode(),ADDR)
	    data,ADDR = detect_s.recvfrom(BUFFSIZE)
	    print (data)
	except OSError:
	    break
	except OverflowError:
	    break
	finally:
	    j = j+1
	    pass
else:
	#关闭链接
	detect_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	socket.setdefaulttimeout(timeout)
	des_HOST = 'localhost'
	loc_HOST = 'localhost'
	PORT = 22225
	BUFFSIZE = 4096
	ADDR = (des_HOST,PORT)
	sta_PORT = 20000
	print(sta_PORT)
	detect_s.bind((loc_HOST,sta_PORT))
	detect_s.sendto('END'.encode(),ADDR)
	data,ADDR = detect_s.recvfrom(BUFFSIZE)
	print (data)

detect_s.close()

tEnd = time.time()
tRun = tEnd - tStart
print(tStart,tEnd)
print('Running time:%s'%tRun)