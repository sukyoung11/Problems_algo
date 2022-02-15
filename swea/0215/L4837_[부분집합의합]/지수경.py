import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N,K = list(map(int,input().split()))

    cnt = 0
    parts = list(combinations(list(range(1,13)),N))

    for part in parts:
        if sum(part) == K:
            cnt += 1

    print(f'#{t} {cnt}')
