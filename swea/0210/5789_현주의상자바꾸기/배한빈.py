import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    numbers = [0] * N

    for q in range(Q):
        i, j = list(map(int, input().split()))

        for num in range(i-1, j):
            numbers[num] = i

    print(f'#{tc} ', end='')
    print(*numbers, sep=' ')
