import sys

# blue = 1
# white = 0
# N = 2 or 4 or 8 or 16 or 32 or 64 or 128

RESULT = [0, 0]

def binary_search(x: int, y: int, n: int, map_arr: list) -> None:
    # 현 위치의 색 저장
    color = map_arr[x][y]

    # 2중 for문으로 맵을 스캔
    for row in range(x, x + n):
        for col in range(y, y + n):
            # 색깔이 다르면
            if color != map_arr[row][col]:
                # 1, 2, 3, 4분면으로 이동합니다.
                binary_search(x, y, n // 2, map_arr)
                binary_search(x, y + n // 2, n // 2, map_arr)
                binary_search(x + n // 2, y, n // 2, map_arr)
                binary_search(x + n // 2, y + n // 2, n // 2, map_arr)
                # 색이 다르면 바로 리턴
                return None

    # 사각형 완성 = 해당 색깔에 + 1
    RESULT[color] += 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    map_arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    binary_search(0, 0, n, map_arr)
    print(RESULT[0])
    print(RESULT[1])