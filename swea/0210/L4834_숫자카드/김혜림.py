import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = input()       # iterable하게 사용할 것이므로 str형으로 받는다.
    
    counts = [0]*10         # 0~9까지의 숫자가 등장하는 횟수를 세기 위한 리스트
    
    for number in numbers:
        counts[int(number)] += 1
    
    # 최대로 많이 등장하는 숫자(max_idx)와 그 횟수(max_value)를 조건문으로 비교하여 찾는다.
    # 이때, 최대 등장 횟수가 같다면 숫자값이 큰 경우를 출력해야 하므로, for문을 오름차순으로 돌며 조건문에 등호를 추가하면 된다.
    max_value = max_idx = 0
    for idx in range(10):
        if counts[idx] >= max_value:
            max_value = counts[idx]
            max_idx = idx
    
    print(f'#{tc} {max_idx} {max_value}')