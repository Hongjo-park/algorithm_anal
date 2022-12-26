
n = int(input())

array = list(map(int, input().split()))

d = [1]*n
result = list()

for i in range(1, n):
    if array[i - 1] < array[i]:
        d[i] = d[i - 1] + 1


# 부분 수열을 구하여 result 리스트에 넣어줍니다.
t = [array[0]]
for i in range(1, n):
    if d[i  - 1] < d[i]:
        t.append(array[i])
    elif d[i  - 1] > d[i]:
        result.append(t)
        t = [array[i]]
result.append(t)

# result 리스트 중 가장 긴 수열을 추출합니다. => max_arr
max_arr = list()
for row in result:
    if len(max_arr) < len(row):
        max_arr = row

max_d = max(d)

print(d)
print(max_arr)
print(max_d)
