


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    dp = [1 for _ in range(n)]
    
    for i in range(1,n):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))
