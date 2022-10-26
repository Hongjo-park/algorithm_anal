# 저울
def calculrator_of_min_weight(sorted_weight_list: list):
    result = 1 
    for weight in sorted_weight_list:
        if result < weight: return result
        result += weight


if __name__ == '__main__':
    n = int(input())
    print(calculrator_of_min_weight(sorted(list(map(int, input().split())))))
    

