# 금광
# n X m
# 오른쪽, 오른쪽 위, 오른쪽 아래

def to_matrix(l: list, n: int) -> list:
    return [l[i:i+n] for i in range(0, len(l), n)]



if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = to_matrix(list(map(int, input().split())), m)
    
    for j in range(1, m) :
        for i in range(n) :
            if i == 0:
                left_up = 0
            else :
                left_up = dp[i - 1][j - 1]

            if i == n - 1 :
                left_down = 0
            else :
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n) :
        result = max(result, dp[i][m - 1])
    print(result)



