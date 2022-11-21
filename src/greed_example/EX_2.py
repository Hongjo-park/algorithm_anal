
# n = 삼각형의 높이

def sum_of_triangle(l: list, leng: int) -> int:
    for i in range(1, leng):
        for j in range(i + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + l[i][j]
    
    return max(dp[-1])


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for i in range(n)]
    dp[0][0] = arr[0][0]

    print(sum_of_triangle(arr, len(arr)))
