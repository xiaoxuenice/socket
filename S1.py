import socket,threading,time
addr = (socket.gethostbyname(socket.gethostname()),1001) #定义socket绑定的地址，ip地址为本地，端口为1001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #创建一个socket对象
s.bind(addr)            #绑定地址
s.listen(100)
#设置允许连接的客户端数量
while True:
    print('start.........')
    cl, addr = s.accept() #接受客户端的连接请求，cl为此链接创建的一个新的scoket对象，addr客户端地址
    def start():
     while True:
        time.sleep(0.05)
        msg = cl.recv(1024)
        value=msg.decode()
        if value:
            print('{}'.format(value))
        def fasun():
         while True:
            a=input()
            cl.send("{}: {}".format(addr[0],a).encode())
        threading.Thread(target=fasun).start()
    threading.Thread(target=start).start()
