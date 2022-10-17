import heapq
INF = int(1e9)
START = 1

def dijkstra():
    q = []
    # 시작노드로 가기 위한 최단 경로는 0으로 설정하며 힙에 삽입
    heapq.heappush(q, (0, START))
    distance[START] = 0
    while q: # 힙이 비어 있지 않다면
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, u = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[u] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[u]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # relaxation
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    # 노드 개수, 간선 개수 입력받기
    n, m = map(int, input().split())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    graph = [[] for i in range(n+1)]
    # 방문여부 확인을 위한 리스트
    visited = [False] * (n+1)

    # 최단 거리값을 모두 무한으로 초기화
    distance = [INF] * (n+1)
    # 모든 간선 정보 입력받기
    for _ in range(m):
        # u에서 v로 가는 비용 = 1, 양방향
        u, v = map(int, input().split())
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    dijkstra()

    # 0번째는 제외
    del distance[0]

    # 가장 큰 distance
    max_distance = max(distance)

    # list.index()를 사용하면 max_distance를 가진 요소 중에 가장 작은 인덱스를 반환합니다.
    print(distance.index(max_distance) + 1, max_distance, sum(1 for i in distance if i == max_distance))
