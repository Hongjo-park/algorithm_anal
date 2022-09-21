import sys
# DFS : 시간초과
# DP로 설계

# DP : 소문제 = ( 가로, 세로, 대각선 )으로 나눔

# 가로, 세로, 대각선 모양일 때 모두 대각선 이동 가능 ( 맵의 조건이 맞다면 )
# dp[2][r][c] = dp[0][r-1][c-1] + dp[1].. + [dp][2]..
# 세로, 대각선 모양일 때 세로 이동 가능
# dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
# 가로, 대각선 모양일 때 가로 이동 가능
# dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]


def get_dp(n: int) -> list:
    '''
    n에 따른 dp에 초기 모양을 생성합니다.
    '''
    return [[[0] * n for _ in range(0, n)] for _ in range(0, 3)]

def init_dp(dp: list, map: list) -> list:
    '''
    dp 초기화 함수
        1. pipe 시작 위치 초기화 : 항상 가로 모양의 [0][1]의 인덱스
        2. 가로로만 이동할 수 있는 모든 곳을 초기화 : 초기화 하지 않는다면 이동 불가 ( 대각선 )
    '''
    # 초기 위치
    dp[0][0][1] = 1

    # 가로로 이동할 수 있는 곳 초기화
    for i in range(2, n):
        if map[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    return dp

def dp_processor(n: int, dp: list, map: list) -> list:
    '''
    세팅된 DP와 map을 통해 2중 for문으로 DP 수행
    수식은 최상단에 정의된 주석을 따릅니다.
    r: row
    c: column

    첫 위치가 (1, 2)이기 때문에 column은 2부터 시작
    '''
    for r in range(1, n):
        for c in range(2, n):
            # 대각선으로 이동 가능한 경우의 수
            if map[r][c] == 0 and map[r-1][c] == 0 and map[r][c-1] == 0:
                dp[2][r][c] = sum(dp[k][r-1][c-1] for k in range(3))
            
            if map[r][c] == 0:
                # 가로로 이동 가능한 경우의 수
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
                # 세로로 이동 가능한 경우의 수
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
    return dp


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = dp_processor(n=n, dp=init_dp(dp=get_dp(n), map=map_), map=map_)
    print(sum(dp[k][-1][-1] for k in range(3)))
