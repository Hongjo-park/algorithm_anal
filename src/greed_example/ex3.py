


def get_group_count(l: list):
    count = 0
    result = 0
    for row in l:
        count += 1
        if count >= row:
            count = 0
            result += 1
    
    return result
        

if __name__ == '__main__':
    N = int(input())
    print(get_group_count(sorted(list(map(int, input().split())))))




