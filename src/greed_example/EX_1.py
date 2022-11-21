
def get_minimum_count_of_string(s: str) -> int:
    zero_switch_count = len(s.replace('1', ' ').split())
    one_switch_count = len(s.replace('0', ' ').split())
    return zero_switch_count if zero_switch_count < one_switch_count else one_switch_count

def checker_of_string_count(s: str) -> bool:
    return True if s.count('1') == 0 or s.count('0') == 0 else False


if __name__ == '__main__':
    s = input()
    if checker_of_string_count(s):
        print(0)
    else:
        print(get_minimum_count_of_string(s))