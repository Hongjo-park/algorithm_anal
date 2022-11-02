# 인접한 창고가 공격 받으면 : 연속적으로 약탈이 안됨 ?

# dp : n개의 배열
# n_array의 i번째를 결정하여 계속 저장하기
# i번째는 i-1번째까지의 값과 i-2에서 i를 더한 값중 더 큰 값으로 결정
# 0번째부터 시작 -> 
# 1번째부터 시작 -> 


def dp_f(i: int):
    if i == 0 or i == 1:
        dp[i] = max(dp[0], n_array[i])
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + n_array[i])
    
    if i + 1 < n:
        dp_f(i+1)

                            
if __name__ == '__main__':
    n = int(input())
    n_array = list(map(int, input().split()))
    dp = [0] * n
    dp_f(0)

    print(max(dp))