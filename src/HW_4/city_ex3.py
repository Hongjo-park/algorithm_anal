
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


if __name__ == '__main__':
    n, m = map(int, input().split())
    map_array = [list(map(int, input().split())) for _ in range(m)]
