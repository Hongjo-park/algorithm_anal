MODULAR = 1000

def jump_a(a: int, k: int) -> bool:
    # a = 이동하려는 위치
    # k = 현재 위치
    return d[k] <= d[a] + s[a]

def jump_b(b: int, k: int) -> bool:
    # 회색섬 여부 확인
    return (d[k] <= d[b] + s[k]) and a[k]

def solution(a: int, b: int, k: int):
    # 섬에서 출발하는 경우와 돌아오는 경우로 나눠서 구현하는 것이 아닌
    # 두 사람이 동시에 출발한다고 가정하자
    # 같은 섬을 밟으면 안되기 때문에 도착섬으로 가는 2가지 경우를 생각한다.

    # A는 섬에서 출발하는 사람, B는 돌아오는 사람으로 가정
    # A는 d[i+1] <= d[i] + s[i]
    # B는 돌아오는 경우이기 때문에, 다음 섬으로 뛰었을 때, 현재 위치로 돌아올 수 있는지 알아야한다.
    # -> d[i+1] <= d[i] + s[i+1]
    c = 0
    if k == n - 1:
        if jump_a(a, k) and jump_b(b, k): c = 1
        else: c = 0
    else:
        if jump_a(a, k): c += solution(k, b, k + 1) % MODULAR
        if jump_b(b, k): c += solution(a, k, k + 1) % MODULAR
        # 둘 다 이동하지 않은 경우 다음섬으로 이동
        c += solution(a, b, k + 1) % MODULAR 
    return c


if __name__ == '__main__':
    n = int(input())
    d = list()
    s = list()
    a = list()

    # d = 발판의 위치, s = 이동할 수 있는 범위, a = 공주를 안을 수 있는 여부 ( 0이면 돌아올 때 사용하지 못함 )
    for _ in range(n):
        row = list(map(int, input().split()))
        d.append(row[0])
        s.append(row[1])
        a.append(row[2])
    print(solution(0, 0, 1))

