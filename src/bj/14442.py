# 벽 부수고 이동하기 : BFS

# queue 사용
from collections import deque


# 단순 2차원 BFS 사용시 벽을 뚫었는지 안뚫었는지에 대한 여부를 확인하기 어렵다.
# 축을 하나 더 추가하여 이동 거리를 2개를 저장한다.
# 1. 벽을 뚫은 경우
# 2. 벽을 뚫지 않은 경우

# for문에 넣을 direction List
dr = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

def bfs():
    q = deque()
    q.append([0, 0, k])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        
        # 통과 : 마지막 지점까지의 거리를 반환
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for d in dr:
            # 이동할 지점 지정
            nx, ny = x + d[0], y + d[1]

            # 맵 안쪽인가
            if 0 <= nx < n and 0 <= ny < m:
                # 맵에서 방문 가능, 처음 가는 길
                if map_array[nx][ny] == 0 and visited[nx][ny][0] == 0:
                    # 이동 후 queue에 추가
                    visited[nx][ny][0] = visited[x][y][0] + 1
                    q.append([nx, ny, w])
                
                # 이동할 지점이 벽이지만 아직 부수지 않은 경우
                elif map_array[nx][ny] == 1 and w > 0:
                    # 벽을 부수고 queue w에는 1을 더함
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])
    
    # while문 동안 방문하지 못했다면 -1을 반환
    return -1


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    map_array = [list(map(int, input())) for _ in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    print(bfs())