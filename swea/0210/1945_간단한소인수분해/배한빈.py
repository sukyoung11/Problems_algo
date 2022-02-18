import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    a = b = c = d = e = 0

    while N % 11 == 0:
        e += 1
        N //= 11
        if N % 11 != 0:
            break
    while N % 7 == 0:
        d += 1
        N //= 7
        if N % 7 != 0:
            break
    while N % 5 == 0:
        c += 1
        N //= 5
        if N % 5 != 0:
            break
    while N % 3 == 0:
        b += 1
        N //= 3
        if N % 3 != 0:
            break
    while N % 2 == 0:
        a += 1
        N //= 2
        if N % 2 != 0:
            break

    print(f'#{tc} {a} {b} {c} {d} {e}')