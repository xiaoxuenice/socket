import socket
import threading
class QQClient:
    def __init__(self, qq):
        self.qq = qq
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建 socket 客户端
        self.client.connect(("192.168.116.200", 8888))# 连接服务器
        self.client.send(self.qq.encode())# 发送自己的身份，给服务器
    def read_chat(self,socket):  # 谁发送的、发送的内容
        while True:
            try:
                msg = socket.recv(1024).decode()
                print(msg)# 将接收到的信息、打印到控制台上
            except ConnectionResetError:
                print("服务器连接失败、请重新连接~")
                break

    def write_chat(self,socket, to_qq):  # 谁发的、发给谁的、内容
        while True:
            msg = input()
            msg = "{}:   {}".format(to_qq, msg)# 将信息发送给服务器
            try:
                socket.send(msg.encode())
            except ConnectionResetError:
                print("服务器连接失败、请重新连接~")
                break
    def chat(self, to_qq):
        threading.Thread(target=self.read_chat, args=(self.client,)).start()
        threading.Thread(target=self.write_chat, args=(self.client, to_qq)).start()
if __name__ == '__main__':
    self = QQClient("123456")
    self.chat("888888")
