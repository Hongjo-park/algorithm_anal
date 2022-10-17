
####################################################
# 1번 문제
####################################################
from random import randrange
while 1:
    i = randrange(10)
    print(f"선택된 숫자는 {i}, 7이 나올 때까지 다시 뽑기 !!")

    if i == 7:
        print("드디어 7!! 종료")
        break
####################################################

####################################################
# 2번 문제
####################################################
from random import randrange
n = int(input("60만점부터 시작!! 1~20 선택: "))
score = 60

for i in range(1, 21):
    com_num = randrange(1, 21)
    if com_num == n:
        print(f"오늘은 {score}만점!")
        break
    score = score - i
    print(f"행운 수 {com_num} {i}만점 사라짐  {score}만점") 
#################################################### 

####################################################
# 3번
####################################################
from random import randrange
user_win = 0
com_win = 0

for i in range(3):
    com_ans = randrange(0, 2)
    user_ans = int(input("홀 0, 짝 1 입력: "))

    if com_ans == user_ans:
        print("사용자 승")
        user_win = user_win + 1
    else: 
        print("컴퓨터 승")   
        com_win = com_win + 1

print(f"userwin = {user_win}, comwin = {com_win}")

####################################################
# 4번
####################################################
from random import randrange
chip = 10

while 1:
    your_num = randrange(1, 11)
    com_num = randrange(1, 11)

    your_bet = 0
    while 1:
        your_bet = int(input(f"your num = {your_num}, chip = {chip} 배팅(0은 포기): "))

        if chip >= your_bet >= 0:
            break
        
    if your_bet == 0:
        continue

    print(f"com num = {com_num}")
    
    if your_num > com_num:
        chip = chip + your_bet
        print(f"사용자 승! chip = {chip}")
    else:
        chip = chip - your_bet

    if chip <= 0:
        print("chip이 없습니다 !!")
        break
    
####################################################

####################################################
# 5번
####################################################
import os
import time

space = ''
for i in range(3):
    os.system("clear")
    for _ in range(i):
        print(" ", end='')
    print("<#_#>")
    time.sleep(1)
####################################################

####################################################
# 6번
####################################################
import time

m = int(input("분을 입력해주세요!! : "))
s = int(input("초를 입력해주세요!! : "))

print(f"{m}분 {s}초")

count = 0

end = m * 60 + s
while 1:
    time.sleep(1)
    count = count + 1

    if count == end:
        print("그만 튀겨!!")
        break
####################################################    
    
####################################################    
# 7번
####################################################    

import os
import time

m = int(input("분을 입력해주세요!! : "))
s = int(input("초를 입력해주세요!! : "))

end = m * 60 + s

for i in range(end, -1, -1):
    os.system("clear")
    print(f"{m}분 {s}초")
    time.sleep(1)
    s = s - 1

    if s < 0:
        m = m - 1
        s = 59

print("그만 튀겨!!")


####################################################    
# 8번
####################################################

for i in range(1, 10):
    print(f"{i} X {i - (i - 1)} = {i}")
    print(f"{i} X {i - (i - 2)} = {i * 2}")
    print(f"{i} X {i - (i - 3)} = {i * 3}")
    print(f"{i} X {i - (i - 4)} = {i * 4}")
    print(f"{i} X {i - (i - 5)} = {i * 5}")
    print(f"{i} X {i - (i - 6)} = {i * 6}")
    print(f"{i} X {i - (i - 7)} = {i * 7}")
    print(f"{i} X {i - (i - 8)} = {i * 8}")
    print(f"{i} X {i - (i - 9)} = {i * 9}")

####################################################


    



    

    
    

