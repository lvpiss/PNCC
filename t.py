#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import time
import random
import socket

tStart = time.time()

f = open("C:/Users/lee/Documents/code/udp/covert.txt","r")
str = f.read()
print(str)

f.close()

r1 = random.randint(1025,65535)
r2 = random.randint(1025,65535)
r3 = random.randint(1025,65535)
r4 = random.randint(1025,65535)
print(r1,r2,r3,r4)

listrand = [r1,r2,r3,r4]
listabd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = 0

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
i= 0 
listport = []
while i < l:
	listportadd = [dictabd[str[i]][0]] + [dictabd[str[i]][1]] + [dictabd[str[i]][2]] + [dictabd[str[i]][3]]
	listport = listport + listportadd
	i = i + 1
print(len(listport))
print(listport)

tEnd = time.time()
tRun = tEnd - tStart
print(tStart,tEnd)
print('Running time:%s'%tRun)