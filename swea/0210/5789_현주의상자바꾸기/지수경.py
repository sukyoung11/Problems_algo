import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    boxes = [0] * N
    for q in range(Q):
        L, R = list(map(int, input().split()))
        for i in range(L - 1, R):
            boxes[i] = q + 1

    print(f'#{t} {" ".join(map(str, boxes))}')
