import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = int(input())
    a = []

    for i in range(N):
        a.append(numbers % 10)
        numbers //= 10

    num_count = [0] * 10
    for number in a:
        num_count[number] += 1

    index = num_count[0]
    for idx in num_count:
        if index < idx:
            index = idx

    max_num = 0

    for i in range(9, -1, -1):
        if max_num < num_count[i]:
            max_num = num_count[i]
            n = i

    print(f'#{tc} {n} {index}')