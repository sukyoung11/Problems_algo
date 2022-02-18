import sys
sys.stdin = open('input.txt')
# 22:40 start 23:30 end

# numbers 내 max값과 인덱스 반환
def my_max(numbers):
    new_max = numbers[0]
    new_idx = 0
    for idx in range(1, len(numbers)):
        if new_max < numbers[idx]:
            new_max = numbers[idx]
            new_idx = idx
    return [new_idx, new_max]

# numbers 내 min값과 인덱스 반환
def my_min(numbers):
    new_min = numbers[0]
    new_idx = 0
    for idx in range(1, len(numbers)):
        if new_min > numbers[idx]:
            new_min = numbers[idx]
            new_idx = idx
    return [new_idx, new_min]

# 매 dump마다 max-1, min+1 을 반복
# max-min을 반환
def dump(dump):
    for _ in range(dump):
        # max값과 min값이 같을 경우, 0을 반환
        if my_max(numbers)[1] == my_min(numbers)[1]:
            return 0

        # 매번 my_max, my_min 함수를 돌리면 시간이 걸릴 것 같아(?) 변수에 할당
        # 똑같나..? ㅋㅋ
        idx_max_number = my_max(numbers)
        idx_min_number = my_min(numbers)
        numbers[idx_max_number[0]] -= 1
        numbers[idx_min_number[0]] += 1

    return my_max(numbers)[1] - my_min(numbers)[1]

T = 10
numbers = [0] * 100
for tc in range(1, T+1):
    times = int(input())
    val = list(map(int, input().split()))
    for idx in range(100):
        numbers[idx] = val[idx]

    ans = dump(times)
    print(f'#{tc} {ans}')
