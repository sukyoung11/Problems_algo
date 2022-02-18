import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    new_numbers = []

    i = 0
    while numbers:
        if i % 2:
            new_numbers.append(numbers.pop(0))
        else:
            new_numbers.append(numbers.pop())
        i += 1

    ans = ' '.join(map(str, new_numbers))

    print(f'#{tc} {ans}')
