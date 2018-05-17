#! -*- coding:utf-8 -*-

import time
import socket

socket_timeout = 0.1


def tcp_scan(ip,port):
    '''利用socket 发送tcp包，探测端口存活率 

    :param ip: 1.1.1.1  type is string 
    :param port: 22 type is int
    
    Usage::
          >>>
          >>> 
    '''
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #基于简单的TCP扫描
        s.settimeout(socket_timeout)
        c=s.connect_ex((ip,port))
        if c==0:
            print "%s:%s is open" % (ip,port)
        else:
            # print "%s:%s is not open" % (ip,port)
            pass
    except Exception,e:
        print e
    
    s.close()


if __name__=="__main__":

    s_time = time.time()

    ip = "14.215.177.38"

    for port in range(0,1024):
        ''' 此处可用协作 '''
        tcp_scan(ip,port)
        
    e_time = time.time()

    print "scan time is ",e_time-s_time






