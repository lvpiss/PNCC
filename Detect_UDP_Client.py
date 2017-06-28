#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import datetime
import time
i = 1
# 系统本身占用的端口号
er_port = []
# 运行起始时间
tStart = datetime.datetime.now()

tStart0 = time.ctime()
tStart1 = str(tStart0).replace(' ','').replace(':','-')
s1 = tStart1[0:7]
s2 = tStart1[7:15]
s3 = tStart1[15:19]
tStart1 = s3+s1+" "+s2
f = open("C:/wget/0213/Send"+tStart1+".txt","a+")
f.close()
timeout = 1
while (i<=64511):
    t1 = datetime.datetime.now()
    t1 = str(t1)
    t1 = t1.replace(".","")
    t1_int = int(str(t1)[-8:-1])
    print("first"+str(t1_int))
    while True:
        try:
            t2 = datetime.datetime.now()
            t2 = str(t2)
            t2 = t2.replace(".","")
            t2_int = int(str(t2)[-8:-1])
            print(t1)
            print(t1_int)
            print(t2_int)
            print("t2_int-t1_int:"+str(t2_int-t1_int))
            if ((t2_int-t1_int)>500 or (t2_int-t1_int)<0):
                break
        except ValueError:
            break
    detect_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socket.setdefaulttimeout(timeout)
    des_HOST = 'localhost'
    loc_HOST = 'localhost'
    PORT = 22232
    BUFFSIZE = 4096
    ADDR = (des_HOST,PORT)
    sta_PORT = 1024+i
    try:
        detect_s.bind((loc_HOST,sta_PORT))
        detect_s.sendto(str(sta_PORT).encode(),ADDR)
        data,ADDR = detect_s.recvfrom(BUFFSIZE)
        print (data)
        f = open("C:/wget/0213/Send"+tStart1+".txt","a+")
        f.write(str(i)+"\n")
        f.close()
        if str(data) == 'End connetting':
            break
        pass
    except OSError:
        er_port.append(i+1024)
    except OverflowError:
        break
    finally:
        i = i+1
        detect_s.close()
        pass

print ("Error port:"+str(len(er_port)))
print(er_port)
tEnd = datetime.datetime.now()
print ("Running time(s): "+str((tEnd-tStart).seconds))
f = open("C:/wget/0213/Send"+tStart1+".txt","a+")
f.write("Error port:"+str(len(er_port))+"\n")
f.write(str(er_port)+"\n")
f.write("Running time(s): "+str((tEnd-tStart).seconds)+"s")
f.close()