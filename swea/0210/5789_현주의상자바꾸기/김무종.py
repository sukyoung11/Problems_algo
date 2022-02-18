import sys
sys.stdin = open('input.txt')

def get_box(n):
    box = [0] * N
    idx = 1
    while idx < n + 1:
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box[j] = idx
        idx = idx + 1
    return ' '.join(map(str, box))

T = int(input())
for i in range(1, T+1):
    N, Q = map(int, input().split())
    print(f'#{i}', get_box(Q))