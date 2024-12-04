import random
import socket

def client_dh():
    # 连接服务器
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.21.171', 12345))
    
    # 接收服务器发送的公共参数
    data = client.recv(1024).decode()
    p, g, B_pub = map(int, data.split(','))
    print(f"接收到服务器发送的素数 p = {p}, 原根 g = {g}, 公钥 B_pub = {B_pub}")
    
    # 生成客户端的私钥和公钥
    a = random.randint(1, p - 1)
    A_pub = pow(g, a, p)
    print(f"客户端生成私钥: {a}, 公钥: {A_pub}")
    
    # 发送公钥给服务器
    client.sendall(str(A_pub).encode())
    
    # 计算共享密钥
    K_A = pow(B_pub, a, p)
    print(f"客户端计算的共享密钥: {K_A}")
    
    client.close()

client_dh()
