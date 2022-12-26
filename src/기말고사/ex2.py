

n, m= map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

# Dynamic Programming을 위한 2차원 DP 테이블 초기화

d = [[-1]*(m) for _ in range(n)]

d[0][0] = array[0][0]

for i in range(0, n):
    for j in range(0, m):
        if i == 0 and j == 0: continue
        if j > 0: # 왼쪽에서 왔냐 ?
            left = d[i][j - 1]
        else: left = 0
        if i > 0: # 위에서 내려왔냐 ?
            up = d[i - 1][j]
        else: up = 0
        if j > 0 and i > 0: # 대각선에서 내려왔냐 ?
            left_up = d[i - 1][j - 1]
        else: left_up = 0
        # 위, 왼쪽, 왼쪽 위 중에서 최대 값과 현재 위치값을 더한 뒤 dp 테이블에 저장
        d[i][j] = max(left, up, left_up) + array[i][j]

print(d[n-1][m-1])

