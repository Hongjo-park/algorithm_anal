

def dp(l: list, dp_l: list):
    for i in range(n):
        for j in range(i):
            if l[i] < l[j]:
                dp_l[i] = max(dp_l[i], dp_l[j]+1)

    return len(l) - max(dp_l)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    dp_arr = [1] * n

    print(dp(arr, dp_arr))