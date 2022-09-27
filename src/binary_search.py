# 반복문
# arr: 리스트, key: 탐색하고자 하는 값, start, end
def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key: return mid
        elif arr[mid] > key: end = mid - 1
        else: start = mid + 1
    return None

# n(원소 개수), target(찾고자 하는 값) 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이분 탐색 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다. ")
else:
    print(result)


# 재귀

# arr: 리스트, key: 탐색하고자 하는 값, start, end
def binary_search(arr, key, start, end):
    if start > end: return None
    mid = (start + end) // 2
    if arr[mid] == key: return mid
    elif arr[mid] > key: return binary_search(arr, key, start, mid - 1)
    else: return binary_search(arr, key, mid + 1, end)

# n(원소 개수), target(찾고자 하는 값) 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))
# 이분 탐색 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다. ")
else:
    print(result)