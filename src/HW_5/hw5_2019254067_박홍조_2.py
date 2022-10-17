INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

# A, B 입력 받은 후 가중치를 1로 설정, 단방향
for i in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1

#자기 자신에게 가는 비용은 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

# Floyd-Warshall 알고리즘 수행
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])


# Graph를 탐색하여 n행과 n열에 INF가 아닌 값의 Count를 저장
# Count가 graph[n][n]인 0까지 포함하여 N개라면 정확한 순위를 알 수 있는 노드이다.
# -> 자기가 바라보는 노드 = 자신보다 위에 있는 노드의 수
# -> 자신을 바라보는 노드 = 자신보다 아래에 있는 노드의 수
# 위 두 노드의 합이 N-1이면 정확한 순위 파악 가능
cnt = 0
result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N:
        result += 1
    cnt = 0

print(result)