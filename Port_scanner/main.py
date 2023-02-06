import socket

scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "199.15.163.128"
port = 443

def portscan(port):
    if scan.connect_ex((host,port)):
        print('Port %d is closed' % port)
    else:
        print('Port %d is open' % port)
portscan(port)
