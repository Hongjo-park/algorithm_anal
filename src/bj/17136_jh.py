arr =[list(map(int,input().split())) for _ in range(10)]
count = [5,5,5,5,5]
result = 101

def attach(x,y,cnt):
    global count
    if x >= 10:
        print('test')
        print(cnt)
        result = min(result,cnt)
        return

    if y>=10:
        try:
            attach(x+1,0,cnt)
        except Exception as e:
            print(e)
        return

    if arr[x][y] == 1:
        # for문으로 5개 종류의 종이 탐색하기
        for k in range(1,6):

            # 여기서 5회 사용한 경우를 잡는다
            if count[k-1] == 0 :
                continue
            
            # 범위를 넘어가면 하지 않는다.
            if x+k >=10 or y+k>= 10:
                continue
            # 이제 여기서는 탐색을 진행해줘야하는데 흠... 고민
            # 2중 for문을 통해서 종이 사이즈만큼 1이 채워져있는지 확인한다.
            # 확인 후에 flag값을 통해서 1을 0으로 전환하는 작업을 해준다.
            # 그리고 count[k]의 값을 
            flag = 1
            for i in range(x,x+k+1):
                for j in range(y,y+k+1):
                    if arr[i][j] == 0 :
                        flag = 0
                        break
                if not flag:
                    break

            if flag:
                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        arr[i][j] = 0
                
                count[k-1]-=1
                attach(x,y+k+1,cnt+1)
                count[k-1]+=1

                for i in range(x,x+k+1):
                    for j in range(y,y+k+1):
                        arr[i][j] = 1
                
    else:
        attach(x,y+1,cnt)

attach(0,0,0)

print(result) if result!= 101 else print(-1)