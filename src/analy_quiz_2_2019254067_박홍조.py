# N <= 200,000
# C <= N

# 인접한 공유기의 최대 거리
# mid보다 크면 설치 -> 개수가 C보다 같거나 큰지 비교

# start가 end와 같거나 클 때의 mid값을 리턴한다 (이 때의 mid는 가장 인접한 두 공유기의 거리가 된다.)


def insert_wifi(array: list, start: int, end: int, result: int) -> int:
    if start >= end: return result

    # mid 설정
    mid = (start + end) // 2

    # 설치할 공유기 수
    cnt = 1

    # 두 위치를 비교할 때 쓰일 변수
    cur = array[0]
    # cur와 집의 위치를 비교한다.
    for row in array:
        if row - cur >= mid:
            # mid보다 같거나 커서 설치 조건에 부합하면 cur를 설치한 집의 위치로 변경
            cnt += 1
            cur = row
            
    # 같거나 크다면 : start = mid + 1로 하여 조금 더 end와 가까이 해본다.
    # 설치 개수가 C보다 작다면, end = mid로 설정하여 설치 개수를 늘려본다.
    return insert_wifi(array, mid + 1, end, mid) if cnt >= c else insert_wifi(array, start, mid, result)
        


if __name__ == '__main__':
    n, c = map(int,input().split())
    house_array = [int(input()) for _ in range(n)]
    house_array.sort()
    max_house_distance = house_array[-1] - house_array[0]

    # 공유기 수가 두개라면 가장 먼 집에 설치
    if c == 2: print(max_house_distance)
    else: print(insert_wifi(house_array, 1, max_house_distance, 0))

