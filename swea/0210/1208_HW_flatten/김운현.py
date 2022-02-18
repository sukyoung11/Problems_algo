import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()

    for i in range(dump):
        boxes[0] += 1
        boxes[99] -= 1
        boxes.sort()

    result = boxes[99] - boxes[0]

    print(f'#{tc} {result}')
