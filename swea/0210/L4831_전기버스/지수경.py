import sys
sys.stdin = open('input.txt')

t = int(input())
for i in range(1, t + 1):

    k, n, m = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    cnt = 0
    now = 0

    while now < n - k:
        drive = list(range(now + 1, now + k + 1))
        chargers = [charger for charger in drive if charger in stations]

        if chargers == []:
            cnt = 0
            break

        else:
            now = chargers[-1]
            cnt += 1

    print(f'#{i} {cnt}')
