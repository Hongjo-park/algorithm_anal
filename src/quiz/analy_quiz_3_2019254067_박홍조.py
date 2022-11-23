

# 계단은 한 계단 또는 두 계단씩 올들 수 있다.
# -> 한 계단을 밟으면서 이어서 다음 계단 또는 다음 다음 계단으로 오를 수 있다.

# 연속된 세 개의 계단을 모두 밟아서는 안된다. ( 시작점 제외 )
# -> if flag >= 3: pass 

# 마지막 도착 계단은 반드시 밟아야한다.
# if i + 1 == n -> 반드시 선택

# dp[i] = l[i], l[i + 1]

def max_of_dp(l: list[int], dp_arr: list[int], n: int) -> int:
    # 한칸, 두칸 중 선택 -> 이미 한칸 올랐다면 다음이랑 다다음 중 더 큰 거 선택
    # 새롭게 올라야되면 다음, 다다음 칸의 합과 다다다음칸을 비교하여 연속해서 갈건지, 두칸 한번에 갈건지 선택
    # 3연속인지 확인 -> flag
    # 마지막인지 확인 i + 1 == n
    flag = 0
    for i in range(n - 1):
        if i + 2 == n:
            dp_arr[i] = l[i + 1]
            break
        elif flag == 2:
            flag = 0
            continue
        else:
            if l[i] + l[i + 1] > l[i + 2] and flag == 0:
                dp_arr[i] = l[i]
                flag += 1
            elif flag == 1:
                dp_arr[i] = max(l[i], l[i + 1])
                flag += 1

    return sum(dp_arr)

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dp = [0] * n

    print(max_of_dp(arr, dp, n))




