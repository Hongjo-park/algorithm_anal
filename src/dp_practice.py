


# basic fibo
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


# Top-down Fibo
dp_td = [0] * 100

def dp_fibo_td(n):
    if n == 1 or n == 2:
        return 1
    
    if dp_td[n] != 0:
        return dp_td[n]
    
    dp_td[n] = fibo(n - 1) + fibo(n - 2)
    return dp_td[n]

# bottom-up Fibo
dp_bp = [0] * 100
dp_bp[1] = 1
dp_bp[2] = 2

def dp_fibo_bp(n):
    for i in range(3, n + 1):
        dp_bp[i] = dp_bp[i - 1] + dp_bp[i - 2]

    return dp_bp[n - 1]


if __name__ == '__main__':
    # print(fibo(50))
    print(dp_fibo_bp(50))