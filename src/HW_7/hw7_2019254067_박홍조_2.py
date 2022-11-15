
# 세가지 능력은 모두 다르다고 한다면
# n번째 위치로 오는 경우는 3가지이다.
# 그 중 소요 시간이 가장 낮은 위치를 뽑는다.

# n번째 위치는 다음과 같다. dp[n] = dp[n - arr[0~2]] + 1
# (n - ( 각 능력 값들 )) 위치에서 소요시간 1초를 더해준다. 이 중 가장 최소 값으로 채택 !
# 소요시간은 시작 위치인 a보다 크다.

INF = 10001

def catch_a_criminal(a: int, b: int, l: list) -> int:
    if a == b: return 0
    # dp 테이블 초기화
    dp = [INF] * (b + 1)
    dp[a] = 0
    
    # a + 1번째부터 채워나갑니다.
    for i in range(a + 1, b + 1):
        for j in l:
            # 능력을 사용하여 이동할 수 있는 거리라면 소요시간을 채워줍니다.
            if i - j >= a:
                dp[i] = min(INF, dp[i - j] + 1)

    # 이동하지 못했다면 -1을 반환합니다.
    if dp[b] == INF: return -1
    return dp[b]



if __name__ == '__main__':
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    print(catch_a_criminal(a, b, arr))