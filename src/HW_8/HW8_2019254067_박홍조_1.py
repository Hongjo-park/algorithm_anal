import re

PLUS = 1
MINUS = 0

def change_operator(s: str) -> int:
    return PLUS if s == '+' else MINUS 

def calculator_min_number(numbers: list[int], operators: list[int]):
    result = numbers[0]
    flag = 0
    for i, row in enumerate(operators):
        if row == PLUS:
            if flag == 0:
                result += numbers[i + 1]
        else:
            if flag != 0:
                result -= sum(numbers[flag:i + 2])
                flag = 0
            else:
                flag = i + 1

    if flag != 0:
        result -= sum(numbers[flag:])
    
    return result


if __name__ == '__main__':
    str_numbers : str = input()
    numbers : list[int] = list(map(int, re.split('[+-]', str_numbers)))
    operators = list(map(change_operator, re.sub('[0-9]', ' ', str_numbers).split()))
    print(calculator_min_number(numbers, operators))

    
