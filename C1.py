import socket
ip=socket.gethostbyname(socket.gethostname())
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect(('192.168.116.100',1001))
    for i in range(1,2):
        s.send("{}EOF  {}      what are you doing?".format(ip,i).encode()) 
        time.sleep(0.05)
except Exception as f :
    print(f,"连接失败")
else:
    
    print('发送成功')
