
def cut_rice_cake(array: list, cut_line: int) -> int:
    '''
    Example:
        array: [1, 2, 3]
        cut_line : 2

        return : 3

    떡의 길이를 가지고 있는 array와 자를 길이를 입력 받습니다.

    해당 길이로 자를 수 있는 모든 길이의 합을 반환합니다.
    '''
    return sum([row - cut_line for row in array if row > cut_line])

def set_binary_search(total: int, m: int, start: int, mid: int, result: int):
    '''
    손님이 원하는 떡의 길이 m보다 자른 떡의 길이가 작은 경우와
    자른 떡의 길이가 더 긴 경우에 대한 처리입니다.

    자른 떡의 길이가 작은 경우
        end = mid - 1로 조정합니다.

    자른 떡의 길이가 더 긴 경우
        result = mid로 설정합니다.
        start = mid + 1로 조정합니다.
    '''
    return (start, mid - 1, result) if total < m else (mid + 1, end, mid)


if __name__ == '__main__':
    start = 1
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    end = max(array)
    result = 0

    while start <= end:
        mid = (start+end)//2
        
        start, end, result = set_binary_search(
            cut_rice_cake(array, mid),
            m,
            start,
            mid,
            result
        )

    print(result)
