

def max_of_dp(l: list[int], dp_arr: list, n: int) -> int:
    # dp로 특정 칸의 계단을 밟았을 때의 최대값을 저장해나갑니다.

    # 처음 3개의 계단에 대해 하드코딩
    # 첫계단을 밟았을 때 -> 0, 두번째 계단 -> 0 + 1 or 1
    # 세번째 계단 -> 0 + 2 or 1 + 2
    if n == 1: return l[0]
    elif n == 2:
        dp_arr.append(l[0])
        dp_arr.append(max(l[0] + l[1], l[1]))
        return dp_arr.pop()

    dp_arr.append(l[0])
    dp_arr.append(max(l[0] + l[1], l[1]))
    dp_arr.append(max(l[0] + l[2], l[1] + l[2]))

    # 현재 계단을 밟았을 때 -> 두칸을 이동했을 때 ( 두칸 전 dp + 현재 계단 값)
    # 연속하여 밟았을 때 -> dp 세 칸 전 -> 두 칸 뛰고 한 칸 뛰기
    for i in range(3, n):
        dp_arr.append(max(dp_arr[i - 2] + l[i], dp_arr[i - 3] + l[i] + l[i - 1]))

    return dp_arr.pop()

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    print(max_of_dp(arr, [], n))