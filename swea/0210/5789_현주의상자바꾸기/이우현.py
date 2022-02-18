import sys
sys.stdin = open('input.txt')

# 40분

T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    list_n = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = list(map(int, input().split()))
        for idx in range(L, R+1):
            list_n[idx] = i
    ans = ' '.join(list(map(str, list_n[1:])))

    print(f'#{tc} {ans}')
