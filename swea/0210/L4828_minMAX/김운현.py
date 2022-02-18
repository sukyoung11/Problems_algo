import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_value = min_value = numbers[0]
    for i in range(N):
        if numbers[i] >= max_value:
            max_value = numbers[i]
    for i in range(N):
        if numbers[i] <= min_value:
            min_value = numbers[i]

    result = max_value - min_value

    print(f'#{tc} {result}')
