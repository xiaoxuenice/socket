import socket,threading

ip = socket.gethostbyname(socket.gethostname())
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.settimeout(3)
    s.connect(('192.168.116.100', 1001))


    def shou():
        while True:
            a = s.recv(1024).decode()
            if a:
                print("\n{}\n".format(a))


    threading.Thread(target=shou).start()
    while True:
        a = input()
        s.send('{}: {}'.format(ip, a).encode())
except Exception as f:
    print(f, "连接失败")
else:

    print('发送成功')
