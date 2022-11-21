

def get_sum_number(n: int, k: int, l: list) -> int:
    return l[0] if (n + 1) % k != 0 else l[1]

def calculator_big_number(m: int, k: int, l: list) -> int:
    return sum(get_sum_number(i, k, l) for i in range(m))


if __name__ == '__main__':
    _, m, k = map(int, input().split())
    print(calculator_big_number(m, k,
                                sorted(list(map(int, input().split())), reverse=True)))
