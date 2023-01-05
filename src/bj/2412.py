from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, cnt = queue.popleft()
        if y == t:
            return cnt if cnt else -1
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = x + i
                ny = y + j

                if (nx, ny) in arr:
                    queue.append((nx, ny, cnt + 1))
                    arr.remove((nx, ny))

    return -1

if __name__ == '__main__':
    n, t = map(int, input().split())
    arr = set([tuple(map(int, input().split())) for _ in range(n)])

    print(bfs())