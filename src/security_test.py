

def inv_mod(a: int, m: int) -> int:
    result = 0
    for i in range(m):
        if (a*i) % m == 1:
            result = i
    
    return result


if __name__ == '__main__':
    print(inv_mod(11, 26))