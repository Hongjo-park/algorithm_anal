import heapq
INF = int(1e9)

def is_move(x: int, y: int) -> bool:
    return x < 0 or y < 0 or x >= w or y >= h or not nodes[y][x].isdigit()

def is_hole(x: int, y: int) -> bool:
    return x < 0 or y < 0 or x >= w or y >= h or nodes[y][x] == 'H'

def dijkstra():
    distances = [[INF] * w for _ in range(h)]
    distances[start[0]][start[1]] = 0
    pq = list()
    heapq.heappush(pq, [0, start[0], start[1]])

    while pq:
        cost, row, col = heapq.heappop(pq)

        if distances[row][col] < cost: continue

        for x, y in direct:
            next_row, next_col = row, col
            next_cost = 0
            # 이동
            while True:
                if is_move(next_col + x, next_row + y): break
                next_row += y
                next_col += x
                next_cost += int(nodes[next_row][next_col])
            if is_hole(next_col + x, next_row + y): continue
            elif nodes[next_row + y][next_col + x] == 'E':
                next_row += y
                next_col += x
            
            if distances[next_row][next_col] > cost + next_cost:
                distances[next_row][next_col] = cost + next_cost
                heapq.heappush(pq, [cost + next_cost, next_row, next_col])
    
    result = distances[end[0]][end[1]]
    return result if result != INF else -1

# dijkstra로 풀기
# R을 만나면 이전 위치로 돌아가기
# 위아래양옆 이동
# dx dy


if __name__ == '__main__':
    w, h = map(int, input().split())
    direct = [(1,0), (-1, 0), (0, 1), (0, -1)]
    start = [0, 0]
    end = [0, 0]

    # input node and preprocess nodes of START and END 
    nodes = list()
    for i in range(h):
        row = list(input())
        for j, r in enumerate(row):
            if r == 'T':
                row[j] = '0'
                start = [i, j]
            elif r == 'E':
                end = [i, j]
        nodes.append(row)

    print(dijkstra())