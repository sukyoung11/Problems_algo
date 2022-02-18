import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    N = int(input())

    boxes = list(map(int, input().split()))

    drop = 0
    max_box = boxes[0]
    max_fall = 0

    for j in range(1, N):
        if max_box <= boxes[j]:
            if j - drop >= max_fall:
                max_fall = j - drop
            else:
                max_fall = max_fall
            drop = j
            max_box = boxes[j]

    if N - drop > max_fall:
        max_fall = N - drop
    else:
        max_fall = max_fall

    print(f'#{i} {max_fall}')
