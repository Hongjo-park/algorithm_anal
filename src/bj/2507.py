# n번의 입력
# 유시 섬으로부터의 거리, 그 거리에 있는 스프링의 세기, 공주와 같이 사용할 수 있는지에 대한 여부

# 출력 : 공주를 구해오는 경로의 수에 1000을 나눈 값

# 발판을 밟으면 좌 우 중에 발판에 해당하는 범위 내에 있는 또 다른 발판에 갈 수 있다.

if __name__ == '__main__':
    n = int(input())
    d = list()
    s = list()
    a = list()

    # d = 발판의 위치, s = 이동할 수 있는 범위, a = 공주를 안을 수 있는 여부 ( 0이면 돌아올 때 사용하지 못함 )
    for _ in range(n):
        row = list(map(int, input().split()))
        d.append(row[0])
        s.append(row[1])
        a.append(row[2])

    # dp 테이블 초기화
    DP = list()
    for i in range(50):
        DP.append([])
        for j in range(50):
            DP[i].append(0)


    # 방향은 총 2가지 가는 방향과 오는 방향
    # 올 때는 a를 확인해야함
    # DP 테이블은 2차원 배열로 구성
    # a -> b로 간다고 했을 때, a < b 라면 후퍼 섬으로 아니라면 유시 섬으로 돌아오는 경우다.
    # a > b 라면 a를 고려

    # DP 테이블 채우기
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                DP[i][j] = 1
            elif i != j or (i == n - 1 and j == n - 1):
                # i > j 라면 i번까지의 발판들 확인
                # 발판의 위치 + 이동 거리가 i번째 발판보다 크다면 DP 테이블 업데이트
                if i > j:
                    for k in range(i):
                        # k번째에서 뛰는 것이기 때문에 s[k]로 비교
                        if d[k] + s[k] >= d[i]:
                            DP[i][j] += DP[k][j]
                elif a[i] != 0:
                    for k in range(j):
                        # 반대로 오는 것은 s[j]의 이동거리를 비교
                        if d[k] + s[j] >= d[j]:
                            DP[i][j] += DP[i][k]
            
            # 경우의 수는 미리 모듈러 연산을 해둔다.
            DP[i][j] %= 1000

    # 출력
    print(DP[n-1][n-1])