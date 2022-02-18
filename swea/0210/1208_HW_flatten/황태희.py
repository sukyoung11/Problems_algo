import sys
sys.stdin = open('input.txt')

for count in range(10):
    N = int(input())
    boxes = list(map(int, input().split()))

    for i in range(N):
        min_idx = 0
        max_idx = 0
        for idx in range(1, len(boxes)):
            if boxes[idx] > boxes[max_idx]:
                max_idx = idx
            if boxes[idx] < boxes[min_idx]:
                min_idx = idx
        boxes[min_idx] += 1
        boxes[max_idx] -= 1

    for idx in range(1, len(boxes)):
        if boxes[idx] > boxes[max_idx]:
            max_idx = idx
        if boxes[idx] < boxes[min_idx]:
            min_idx = idx

    print(f'#{count + 1} {boxes[max_idx] - boxes[min_idx]}')