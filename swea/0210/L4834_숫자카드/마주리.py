import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(str, input()))

    counts = [0] * 10
    for num in numbers:
        counts[int(num)] += 1

    max_cnt = max_val = 0
    for i in range(10):
        if counts[i] >= max_cnt:
            max_val = i
            max_cnt = counts[i]

    print(f'#{tc} {max_val} {max_cnt}')