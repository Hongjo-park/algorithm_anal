# DFS로 2D 맵에서 주어진 블럭을 만들기
# 1. ㅗ 모양은 시작 지점이 아닌 이미 한 번 탐색이 이루어졌을 때, 생성이 가능하다.
# 2. 모든 블럭은 4칸을 차지한다. 


def is_run(row: int, col: int, visit_map: list) -> bool:
    '''
    방문하려는 곳의 row와 column이 0 이상이고 n과 m 사이에 있어야하며, 

    방문 여부를 확인하는 2차원 list [n,m]에 방문한 적이 없어야한다.
    '''
    return True if 0 <= row < n and 0 <= col < m and visit_map[row][col] == 0 else False


def dfs(row: int, col: int, idx: int, total: int) -> None:
    global answer
    # answer가 최대인지를 확인하고 Return
    if answer >= total + max_val * (3 - idx):
        return None

    # 모든 블럭을 다 돈 경우 answer를 입력해준다. ( 이번 누적합 total과 이전 누적합 answer를 비교한다 )
    if idx == 3:
        answer = max(answer, total)
        return None
    else:
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if is_run(nr, nc, visit):
                if idx == 1:
                    # ㅗ 모양의 블럭 만들기 ( 다음 블럭을 탐색하는 것이 아닌 기존 블럭을 탐색합니다. )
                    visit[nr][nc] = 1
                    dfs(row, col, idx + 1, total + array[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + array[nr][nc])
                visit[nr][nc] = 0

if __name__ == '__main__':
    # 입력
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    # 0으로 채워진 n*m 2차원 List[int] 생성
    visit = [([0] * m) for _ in range(n)]
    # 이동을 결정할 direction list ( row, col )
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    answer = 0
    # 입력받은 array에서의 최대 Value
    max_val = max(map(max, array))
    # 탐색
    for r in range(n):
        for c in range(m):
            visit[r][c] = 1
            dfs(r, c, 0, array[r][c])
            visit[r][c] = 0
    print(answer)