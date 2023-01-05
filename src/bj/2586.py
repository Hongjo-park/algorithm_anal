


def solution(f_index: int, h: int):
    global min_h
    if f_index == f:
        min_h = min(min_h, h)
        return None
    
    for i in range(p):
        if pivot[i] == 0:
            pivot[i] = 1
            h += abs(p_arr[i] - f_arr[f_index])
            solution(f_index + 1, h)
            h -= abs(p_arr[i] - f_arr[f_index])
            pivot[i] = 0
            

if __name__ == '__main__':
    p, f = map(int, input().split())
    p_arr = list(map(int, input().split()))
    f_arr = list(map(int, input().split()))
    pivot = [0] * p
    min_h = 0x7fffffff
    
    solution(0, 0)
    print(min_h)
