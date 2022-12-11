

if __name__ == '__main__':
    n = int(input())
    print(sorted(list(map(int, input().split())))[(n-1)//2])