# 개똥벌레
import sys
input = sys.stdin.readline

def broken_hurdle(array: list, x: int):
    '''
    --------------------------
    Example:
        array = [1, 2, 4]
        x = 3

        Return : 2
    --------------------------
    오름차순 정렬된 array에서 x가 삽일될 인덱스를 반환합니다.
    
    즉 배열에서 파괴한 장애물 수를 얻을 수 있습니다.
    '''
    lo=0
    hi = len(array)
    while lo < hi:
        mid = (lo+hi)//2
        if array[mid] < x: lo = mid+1
        else: hi = mid
    return lo


if __name__ == '__main__':
    # 입력
    n, h = map(int,input().split())
    cave_array = [int(input().rstrip()) for _ in range(n)]

    # 전체 동굴의 배열 중 석순과 종유석으로 나눕니다.
    top, bottom = list(), list()
    for i in range(n):
        if i % 2 == 0:
            bottom.append(cave_array[i])
        else:
            top.append(cave_array[i])
    # 석순과 종유석의 배열들을 정렬합니다.
    top.sort()
    bottom.sort()

    # cnt : 최소장애물 경로의 개수를 세기 위한 변수입니다.
    cnt = 1
    # min_value : 최소장애물 경로의 높이를 저장하는 변수입니다.
    min_value = float('inf')
    for row in range(1, h + 1):
        # 전체 장애물 돌파 수 = 부셔진 석순 개수 + 종유석 개수
        total_cnt = n - (broken_hurdle(bottom, row) + broken_hurdle(top, h+1 - row))

        if total_cnt < min_value:
            # 최소장애물 수 및 경로 개수 초기화
            min_value = total_cnt
            cnt = 1
        elif total_cnt == min_value:
            # 최소장애물 수 경로 ++
            cnt += 1
    
    print(min_value, cnt)

    
