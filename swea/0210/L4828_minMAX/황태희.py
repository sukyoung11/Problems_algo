import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    min_num = max_num = numbers[0]

    for number in numbers[1:]:
        if min_num > number:
            min_num = number

        if max_num < number:
            max_num = number

    print(f'#{tc + 1} {max_num - min_num}')