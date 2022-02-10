import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1,T+1):
    dump = int(input())
    boxes = list(map(int,input().split()))

    for i in range(dump+1):

        # max(), min() 없이 max, min 구하기
        max_num = min_num = boxes[0]
        for box in range(1, 100):
            if boxes[box] >= max_num:
                max_num = boxes[box]
            if boxes[box] <= min_num:
                min_num = boxes[box]

        # 최고점의 위치 찾기, -1
        for box_num in range(len(boxes)):
            if boxes[box_num] == max_num:
                boxes[box_num] -= 1
                break

        # 최저점의 위치 찾기, +1
        for box_num in range(len(boxes)):
            if boxes[box_num] == min_num:
                boxes[box_num] += 1
                break

        # 최고점 - 최저점
        result = max_num - min_num
        if result <= 1:
            break

    print(f'#{t} {result}')