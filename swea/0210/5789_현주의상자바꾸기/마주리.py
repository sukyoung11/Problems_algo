import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for _ in range(L - 1, R):
            boxes[_] = i

    result = ' '.join(str(box) for box in boxes)
    print(f'#{tc} {result}')