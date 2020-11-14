import socket,time
addr = ('192.168.116.100',1001) #定义socket绑定的地址，ip地址为本地，端口为1001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #创建一个socket对象
s.bind(addr)            #绑定地址
s.listen(100)             #设置允许连接的客户端数量
while True:
    cl, addr = s.accept() #接受客户端的连接请求，cl为此链接创建的一个新的scoket对象，addr客户端地址
    msg = cl.recv(1024)
    value=msg.decode()
    print(value)
    if value == 'go':
        print("go")
    elif value == 'ba':
        print("ba")
    elif value == 'le':
        print("le")
    elif value == 'ri':
        print("ri")
    else:
        print("stop")
