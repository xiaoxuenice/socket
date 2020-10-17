import socket
import threading
def server_chat(socket, socket_mapping):
    #qq用户身份id
    qq = socket.recv(1024).decode()
    # 存储身份(这里也可以实现不允许同一账户多次登录)
    socket_mapping[qq] = socket
    # 给所有socket 显示 该用户上线了
    for k, v in socket_mapping.items():
        v.send(f"【{qq}】上线了".encode())

    # 开启循环、用来不断的进行转发数据
    while True:
        try:
            # 接收客户端发送的信息
            data = socket.recv(1024).decode()
            to_qq, msg = data.split(":", 1)
            # 将信息转发给 to_qq 对应的客户端
            to_socket = socket_mapping[to_qq]
            # 将信息发送给 to_socket
            to_socket.send(f"{qq}:{msg}".encode())
        except ConnectionResetError:
            # 该客户端离线了
            socket_mapping.pop(qq)
            # 提示所有的客户端、该用户下线了
            for k, v in socket_mapping.items():
                v.send(f"【{qq}】下线了".encode())
            # 退出循环
            break
        except KeyError:
            # 该用户不在线、提示fqq,您的好友不在线
            socket.send(f"您的好友【{to_qq}】不在线".encode())
if __name__ == '__main__':
    # 初始化socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP地址和端口
    server.bind(("192.168.116.100", 8888))
    # 设置最大监听数
    server.listen(100)
    # 设置一个字典，用来保存每一个客户端的连接 和 身份信息
    socket_mapping = {}
    # 开启准备等待获取客户端的链接
    while True:
        sc, addr = server.accept()
        # 为每一个客户端开启一个线程、保证程序的高效运行
        threading.Thread(target=server_chat, args=(sc, socket_mapping)).start()

