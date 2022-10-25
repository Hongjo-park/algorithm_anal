

def inv_mod(a: int, m: int) -> int:
    result = 0
    for i in range(m):
        if (a*i) % m == 1:
            result = i
    
    return result


if __name__ == '__main__':
    z = [(row, inv_mod(row, 26)) for row in range(1, 26) if inv_mod(row, 26)]
    for row in z:
        print(row)
