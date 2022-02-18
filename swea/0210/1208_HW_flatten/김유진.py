import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    long = len(boxes)
    count = 0
    while count < N:
        list.sort(boxes)
        if max(boxes) != min(boxes):
            boxes[long-1] -= 1
            boxes[0] += 1
            difference = max(boxes)-min(boxes)
            count += 1
        else:
            difference = 0
            break;

    print(f'#{tc} {difference}')
