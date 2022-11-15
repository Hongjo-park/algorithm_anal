




def get_efficient_bill(m: int, l: list) -> int:
    # dp 테이블 초기화
    dp = [100001] * (m + 1)
    dp[0] = 0
    

    for i in range(n):
        for j in range(l[i], m + 1):
            # (i - k)원을 만드는 방법이 존재하는 경우
            if dp[j - l[i]] != 10001:
                dp[j] = min(dp[j], dp[j - l[i]] + 1)

    # m원을 만드는 경우의 수가 없는 경우 -1을 반환합니다.
    if dp[m] == 10001:
        return -1

    # 만들 수 있다면 dp[m]을 반환합니다.
    return dp[m]


if __name__ == '__main__':
    n, m = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    print(get_efficient_bill(m, coins))