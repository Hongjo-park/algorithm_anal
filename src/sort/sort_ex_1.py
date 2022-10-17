

def pipe_ex_1(k: int, a: list, b: list):
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
    return a


if __name__ == '__main__':
    n, k = map(int, input().split())
    array_a = sorted(list(map(int, input().split())))
    array_b = sorted(list(map(int, input().split())), reverse=True)

    print(sum(pipe_ex_1(k, array_a, array_b)))

