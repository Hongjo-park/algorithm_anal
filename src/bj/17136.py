# 색종이 붙이기 

# 1, 4, 9, 16, 25 넓이의 정사각형 색종이 존재

# 맵에서 1을 찾으면 만들 수 있는 최대 길이를 설정합니다.
# 최대 길이에서 1씩 빼면서 다양한 색종이를 만들어봅니다.
# 색종이를 모두 다 덮었다면 색종이의 개수를 answers에 저장합니다.
#  - 다른 크기의 색종이로 넘어가기 전에는 맵을 초기화합니다.
#  - 다양한 색종이들에 대한 결과들이 저장됩니다.

# answers 중에 -1을 제외하고 0 이상의 값이 있다면 출력합니다.
# - 0 이상의 값이 없다면 -1을 출력합니다.

def find_max_length(y: int, x: int) -> int:
    length = 1
    for l in range(2, min(10 - y, 10 - x, 5) + 1):
        for i in range(y, y + l):
            for j in range(x, x + l):
                if arr[i][j] == 0:
                    return length
        length += 1
    return length

def cover(y: int, x: int, length: int, c: int) -> None:
    for i in range(y, y + length):
        for j in range(x, x + length):
            arr[i][j] = c

def dfs(count: int) -> int:
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                # 최대길이 ~ 1까지 색종이 만들기
                for l in range(find_max_length(i, j), 0, -1):
                    if papers[l]:
                        # 색종이 덮기
                        cover(i, j, l, 0)
                        papers[l] -= 1
                        # 재귀 및 결과 저장
                        answers.add(dfs(count + 1))
                        # 맵, 색종이 개수 초기화
                        cover(i, j, l, 1)
                        papers[l] += 1
                if answers: return min(answers)
                else: return -1
    return count


if __name__ == '__main__':
    arr = [list(map(int, input().split())) for _ in range(10)]
    papers = [0, 5, 5, 5, 5, 5]
    answers = set()
    answers.add(dfs(0))
    if -1 in answers:
        answers.remove(-1)
    print(min(answers) if answers else -1)

