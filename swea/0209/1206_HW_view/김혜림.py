import sys
sys.stdin = open('input.txt')

T = 10


def get_min(*args):
    min_value = args[0]
    for arg in args:
        if arg < min_value:
            min_value = arg
    return min_value


for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    total = 0
    
    for idx in range(2, N-2):
        if numbers[idx] > numbers[idx+1] and numbers[idx] > numbers[idx-1]:
            if numbers[idx] > numbers[idx+2] and numbers[idx] > numbers[idx-2]:
                box = get_min(numbers[idx]-numbers[idx-1], numbers[idx]-numbers[idx-2], numbers[idx]-numbers[idx+1], numbers[idx]-numbers[idx+2])
                total += box
    print(f'#{tc} {total}')