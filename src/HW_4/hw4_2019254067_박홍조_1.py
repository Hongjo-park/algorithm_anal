

def dfs(row, col):
    # 맵을 벗어나는 경우 False 반환하여 Count 되지 않게합니다.
    if row <= -1 or row >= n or col <= -1 or col >= m:
        return False
    
    # 맵의 해당 주소가 0이라면 dfs합니다.
    if not map_array[row][col]:
        # 방문한 곳은 1로 채워줍니다
        map_array[row][col] = 1
        # 왼쪽
        dfs(row - 1, col)
        # 오른쪽 
        dfs(row + 1, col)
        # 아래
        dfs(row, col + 1)
        # 위
        dfs(row, col -1)
        # True를 반환하여 Count되게 합니다.
        return True
    return False
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    map_array = [list(map(int, input())) for _ in range(n)]

    # 맵을 탐색합니다.
    print(sum(1 for row in range(n) for col in range(m) if dfs(row, col)))

