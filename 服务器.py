import random
import socket
from sympy import isprime, primitive_root

# 初始化服务器
def server_dh():
    # 生成公共素数和原根
    p, g = generate_prime_and_root()
    print(f"服务器生成素数 p = {p}, 原根 g = {g}")
    
    # 生成服务器的私钥和公钥
    b = random.randint(1, p - 1)
    B_pub = pow(g, b, p)
    print(f'服务器私钥：{b},公钥：{B_pub}')
    
    # 启动Socket服务器
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.21.171', 12345))
    server.listen(1)
    print("\n等待客户端连接...\n")
    
    conn, addr = server.accept()
    print(f"客户端连接: {addr}")
    
    # 发送公共参数
    conn.sendall(f"{p},{g},{B_pub}".encode())
    
    # 接收客户端的公钥
    A_pub = int(conn.recv(1024).decode())
    print(f"接收到客户端公钥: {A_pub}")
    
    # 计算共享密钥
    K_B = pow(A_pub, b, p)
    print(f"服务器计算的共享密钥: {K_B}")
    
    conn.close()
    server.close()

# 生成素数和原根
def generate_prime_and_root():
    while True:
        p = random.randint(100, 255)
        if isprime(p):
            try:
                g = primitive_root(p)
                return p, g
            except ValueError:
                continue

server_dh()
