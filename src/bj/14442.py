# 벽 부수고 이동하기 : BFS

# queue 사용
from collections import deque

# 단순 2차원 BFS 사용시 벽을 뚫었는지 안뚫었는지에 대한 여부를 확인하기 어렵다.
# 축을 하나 더 추가하여 이동 거리를 저장한다.
# [w][x][y]
# w : 벽을 부순 횟수 (k개의 0을 담고 있는 List)

# for문에 넣을 direction List
dr = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        w, y, x = q.popleft()
        
        # 통과 : 마지막 지점까지의 거리를 반환
        if x == m - 1 and y == n - 1:
            return visited[w][y][x]

        for dx, dy in dr:
            # 이동할 지점 지정
            nx, ny = x + dx, y + dy

            # 맵 안쪽인가
            if 0 <= ny < n and 0 <= nx < m:
                # 맵에서 방문 가능, 처음 가는 길
                if map_array[ny][nx] == 0 and visited[w][ny][nx] == 0:
                    # 이동 후 queue에 추가
                    visited[w][ny][nx] = visited[w][y][x] + 1
                    q.append([w, ny, nx])
                
                # 이동할 지점이 벽이지만 아직 부수지 않은 경우
                elif map_array[ny][nx] == 1 and w < k and visited[w + 1][ny][nx] == 0:
                    # 벽을 부수고 queue w에는 1을 더함
                    visited[w + 1][ny][nx] = visited[w][y][x] + 1
                    q.append([w + 1, ny, nx])
    
    # while문 동안 방문하지 못했다면 -1을 반환
    return -1


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    map_array = [list(map(int, input())) for _ in range(n)]
    visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
    print(bfs())