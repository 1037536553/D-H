import random
from sympy import isprime, primitive_root

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

# 机器A
def machine_A(p, g):
    a = random.randint(1, p - 1)  # A的私钥
    A_pub = pow(g, a, p)  # A的公钥
    print(f"机器A生成私钥: {a}, 公钥: {A_pub}")
    return a, A_pub

# 机器B
def machine_B(p, g):
    b = random.randint(1, p - 1)  # B的私钥
    B_pub = pow(g, b, p)  # B的公钥
    print(f"机器B生成私钥: {b}, 公钥: {B_pub}")
    return b, B_pub

# 模拟D-H密钥交换
def simulate_dh_exchange():
    # 1. 生成公共素数和原根
    p, g = generate_prime_and_root()
    print(f"选定素数 p = {p}, 原根 g = {g}\n")
    
    # 2. 机器A生成私钥和公钥
    a, A_pub = machine_A(p, g)
    
    # 3. 机器B生成私钥和公钥
    b, B_pub = machine_B(p, g)
    
    # 4. 机器A计算共享密钥
    K_A = pow(B_pub, a, p)
    print(f"\n机器A计算的共享密钥: {K_A}")
    
    # 5. 机器B计算共享密钥
    K_B = pow(A_pub, b, p)
    print(f"机器B计算的共享密钥: {K_B}\n")
    
    # 6. 验证共享密钥是否一致
    if K_A == K_B:
        print(f"共享密钥一致: K = {K_A}")
    else:
        print("共享密钥不一致，存在问题！")

# 执行模拟
simulate_dh_exchange()
