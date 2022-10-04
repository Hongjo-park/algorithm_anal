
# [-10억 ~ 10억]까지에 대해서만 본다.
maximum = -1e9
minimum = 1e9


def dfs(depth: int, total: int, plus: int, minus: int, multiply: int, divide: int) -> None:
    global maximum, minimum
    # depth는 n까지
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return None

    # + - * /에 따라서 계산한 후 탐색
    if plus:
        dfs(depth + 1, total + sequence[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - sequence[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * sequence[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / sequence[depth]), plus, minus, multiply, divide - 1)


if __name__ == '__main__':
    # 입력
    n = int(input())
    # 수열
    sequence = list(map(int, input().split()))
    # 연산자
    operators = list(map(int, input().split()))
    dfs(1, sequence[0], operators[0], operators[1], operators[2], operators[3])
    print(maximum)
    print(minimum)
