import sys

sys.stdin = open('input.txt')


def func(k, n, m, stops):
    position = 0
    tmp = 0
    cnt = 0
    while position < (n - k):
        for j in range(1, k + 1):
            if (position + j) in stops:
                tmp = j

        if tmp == 0:
            return 0

        position += tmp
        tmp = 0
        cnt += 1
    return cnt


T = int(input())

for i in range(1, T + 1):
    K, N, M = map(int, input().split())
    stop_list = list(map(int, input().split()))
    print(f'#{i}', func(K, N, M, stop_list))
