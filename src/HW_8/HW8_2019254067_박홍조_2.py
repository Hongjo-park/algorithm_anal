
def sorted_meeting_time(l: list[list[int]]) -> list[list[int]]:
    '''
    시작 시간을 기준으로 정렬한 후 다시 끝나는 시간을 기준으로 정렬한다.
    '''
    return sorted(sorted(l, key=lambda x: x[0]), key=lambda x: x[1])


def calculator_max_meeting_room(l: list[list[int]]) -> int:
    '''
    회의실의 시작 시간이 마지막으로 저장된 회의실의 끝나는 시간 이상이라면
    회의실 개수를 추가하고, 마지막 회의실을 바꾸어줍니다.
    '''
    last_time = 0
    meeting_room_cnt = 0
    for i, j in l:
        if i >= last_time:
            meeting_room_cnt += 1
            last_time = j
    
    return meeting_room_cnt


if __name__ == '__main__':
    n : int = int(input())
    arr : list[list[int]] = sorted_meeting_time([list(map(int, input().split())) for _ in range(n)])

    print(calculator_max_meeting_room(arr))

