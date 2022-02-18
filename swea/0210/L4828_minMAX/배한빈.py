import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_value = max_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    answer = max_value - min_value

    print(f'#{tc} {answer}')