

def dfs(row, col):
    if row <= -1 or row >= n or col <= -1 or col >= m:
        return False
    
    if not map_array[row][col]:
        map_array[row][col] = 1
        # 왼쪽
        dfs(row - 1, col)
        # 오른쪽 
        dfs(row + 1, col)
        # 아래
        dfs(row, col + 1)
        # 위
        dfs(row, col -1)
        return True
    return False
        

if __name__ == '__main__':
    n, m = map(int, input().split())
    map_array = [list(map(int, input())) for _ in range(n)]

    print(sum(1 for row in range(n) for col in range(m) if dfs(row, col)))

