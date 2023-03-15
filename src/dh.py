import time
import random

def evaluate_n2(A, x):
    result = 0
    # n^2의 시간복잡도는 x의 계산과 a * x의 계산을 따로합니다.
    for i in range(n):
        # x 계산을 위한 변수
        term_x = 1
        for j in range(i):
            # x가 1차면 시작 term_x인 1 * x로 x
            # x가 n차면 n번 반복
            term_x *= x
        # 계산된 x와 a를 곱셈하여 result에 저장
        result += A[i] * term_x
    return result


def evaluate_n(A, x):
    result = 0
    # n의 시간복잡도는 a와 x의 계산을 한번에 수행합니다.
    for i in range(n):
        # ** 기호는 제곱을 의미합니다.
        result += A[i] * (x ** i)
    return result
    
    # ps. 다음 수식을 통해 한 줄로 작성 가능합니다.
    # return sum(A[i] * (x ** i) for i in range(n))

# ---------- n 입력 및 A, X 설정 ------------ #

n = int(input("입력 크기 : "))
X = random.randint(-1000, 1000)
A = [random.randint(-1000, 1000) for _ in range(n)]

# ---------- n2 시간복잡도 계산 ------------- #
s_n2 = time.process_time()
evaluate_n2(A, X)
e_n2 = time.process_time()
print("n2 수행시간 : ", e_n2 - s_n2)

# ---------- n 시간복잡도 계산 ------------- #

s_n = time.process_time()
evaluate_n(A, X)
e_n = time.process_time()
print("n 수행시간 : ", e_n - s_n)
