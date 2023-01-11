


def table():
    
    pass


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    # DP

    # 0 아빠, 1 엄마, 2 현이

    # 아빠 : 1번자리
    # 엄마 : k + 1번자리
    # 현이 : 2k + 1번자리

    # L = 우측으로 이동
    # R = 좌측으로 이동
    