import sys
sys.stdin = open('input.txt')

def get_flatten(dump, boxes):
    idx = 0
    while True:
        max_box = min_box = boxes[0]
        max_idx = min_idx = 0
        for j in range(len(boxes)):
            if max_box < boxes[j]:
                max_box = boxes[j]
                max_idx = j
            if min_box > boxes[j]:
                min_box = boxes[j]
                min_idx = j
        boxes[max_idx] = max_box - 1
        boxes[min_idx] = min_box + 1
        if idx == dump:
            break
        idx = idx + 1
    return max_box - min_box

for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    idx = 0
    print(f'#{i} {get_flatten(dump, boxes)}')
