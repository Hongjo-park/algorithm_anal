
# 벽 부수고 이동하기 3 : BFS

# queue 사용
from collections import deque

# direction List
dr = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

# 0ㄴ 1ㅂ 2ㄴ 3ㅂ 4 5
# d % 2 == 0: 낮

# 우선순위 큐 사용
 
def bfs():
    q1, q2, q3 = deque(), deque(), deque()
    q1.append([0, 0, 0, 0])
    visited[0][0][0] = 1

    while q1:
        while q1:
            w, y, x, d = q1.popleft()
            
            # 통과 : 마지막 지점까지의 거리를 반환
            if x == m - 1 and y == n - 1:
                return visited[w][y][x]

            for dx, dy in dr:
                nx, ny = x + dx, y + dy

                if 0 <= ny < n and 0 <= nx < m:
                    nd = d + 1
                    if map_array[ny][nx] == 0 and visited[w][ny][nx] == 0:
                        visited[w][ny][nx] = visited[w][y][x] + 1
                        q2.append([w, ny, nx, nd])
                    elif map_array[ny][nx] == 1 and w < k and visited[w + 1][ny][nx] == 0:
                        if d % 2 == 0:
                            visited[w + 1][ny][nx] = visited[w][y][x] + 1
                            q2.append([w + 1, ny, nx, nd])
                        else:
                            visited[w + 1][ny][nx] = visited[w][y][x] + 2
                            q3.append([w + 1, ny, nx, nd + 1])
        q1, q2, q3 = q2, q3, deque()
        if not q1:
            q1, q2 = q2, deque()
                    
    return -1


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    map_array = [list(map(int, input())) for _ in range(n)]
    visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

    print(bfs())
