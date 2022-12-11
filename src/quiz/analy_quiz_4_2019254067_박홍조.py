def min_of_l(l: list[int], n: int) -> int:
    '''
    n(정수)값과 리스트 l의 모든 요소들의 뺄셈의 절대값 중 최소값을 반환합니다.

    l: List[int]
    n : 정수

    return : int
    '''
    return min(abs(n - row) for row in l if n - row != 0)

def solution(l: list[int], n: int, k: int) -> int:
    '''
    List에서 하나의 요소와 나머지 값들의 뺄셈의 절대값들 중 k개의 최소값들의 합을 반환합니다.

    return : int
    '''
    return sum(sorted(min_of_l(l[i + 1:], row) for i, row in enumerate(l) if i + 1 != n)[:k])


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = list(set(map(int, input().split())))
    print(solution(arr, len(arr), k))

