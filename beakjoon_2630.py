import sys

# blue = 1
# white = 0
# N = 2 or 4 or 8 or 16 or 32 or 64 or 128
        
ANSWER = [0, 0]

def traversal(x: int, y: int, N: int, map: list):
    color = map[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != map[row][col]:
                # 각각 1, 2, 3, 4분면 이동
                traversal(x, y, N // 2, map)
                traversal(x, y + N // 2, N // 2, map)
                traversal(x + N // 2, y, N // 2, map)
                traversal(x + N // 2, y + N // 2, N // 2, map)
                return 0
    # 모든 범위 내애 종이 색깔이 같다면
    if color == 0:
        ANSWER[0] += 1
    else:
        ANSWER[1] += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    traversal(0, 0, N, map)
    for a in ANSWER:
        print(a)
