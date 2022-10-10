

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = [i for i in range(m)]
    map_array = [list(map(int, input().split())) for _ in range(n)]

    while True:
        cost = 0
        edges = []
        for _ in range(n):
            u, v, w = map(int, input().split()) #출발점, 도착점, 간선의 가중치
            edges.append((u, v, w))
        edges.sort(key=lambda x: x[2]) #가중치를 중심으로 오름차순으로 정렬해줍니다.

        for edge in edges:
            u, v, w = edge
            if find(u) != find(v): #유니온 파인드로 부모 노드가 같은지 보고, 아니라면 통일해줍니다.
                union(u, v)
            else: #문제에서 원하는 것이 절약되는 액수이므로, 연결되지 않은 간선의 가중치를 더해줍니다.
                cost += w
        print(cost) 
