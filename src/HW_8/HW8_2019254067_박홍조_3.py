
# 2중 for 문으로 N^2번 연산합니다.
# 1억번 연산 가능이기 때문에 N <= 1,000인 경우 연산 가능


def selector_bowling_ball(l: list[int]) -> int:
    '''
    볼링공의 무게가 다른 경우의 수를 모두 뽑은 뒤 2로 나누어줍니다.
    '''
    return sum(1 for i in l for j in l if i != j) // 2


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    print(selector_bowling_ball(arr))

