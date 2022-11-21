

def selector_max_card(l: list) -> int:
    return max(min(row) for row in l)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(selector_max_card([list(map(int, input().split())) for _ in range(n)]))
