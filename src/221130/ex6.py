

def solution(start: int, end: int, l: list) -> int:
    if start > end:
        return -1
    
    mid = (start + end) // 2
    target = l[mid]

    if target == mid:
        return target
    elif mid < target:
        end = mid - 1
    else:
        start = mid + 1
    
    return solution(start, end, l)


if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))

    print(solution(0, n - 1, arr))
