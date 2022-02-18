import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    bus_line = int(input())
    bus_stop = [0] * 5000

    for bus in range(bus_line):
        A, B = map(int, input().split())
        for _ in range(A - 1, B):
            bus_stop[_] += 1

    P = int(input())

    print(f'#{tc} ', end='')
    for p in range(P):
        j = int(input())
        print(f'{bus_stop[j - 1]}', end=' ')
    print('')
