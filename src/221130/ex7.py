from collections import deque

def bfs(graph: list, v: int, distance: list) -> list:
    q = deque([v])
    # 큐가 빌 때까지 반복
    while q:
        v = q.popleft()

        # 현재 정점의 인접 정점 모드 큐에 삽입, 방문
        for i in graph[v]:
            if distance[i] == -1:                
                distance[i] = distance[v] + 1
                q.append(i)
    
    return distance
    

if __name__ == '__main__':
    n, m, k, x = map(int, input().split())
    map_arr = [[] * n for _ in range(n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        map_arr[i].append(j)
    distance = [-1] * (n + 1)
    distance[x] = 0
    
    
    result = [i for i, row in enumerate(bfs(map_arr, x, distance)) if row == k]
    if result:
        for row in result:
            print(row)
    else:
        print(-1)
