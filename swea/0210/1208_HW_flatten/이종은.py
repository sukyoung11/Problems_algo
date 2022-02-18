import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1,T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 처음에 dump != 0으로 했다가, 0이 되는 동시에 dump 횟수 1번 생략한 채 break 되므로 dump >= 0 으로 수정
    while dump >= 0:
        max_box = boxes[0]
        min_box = boxes[0]

        # 가장 높은 박스, 가장 낮은 박스 구하기
        for i in range(len(boxes)):
            if boxes[i] > max_box:
                max_box = boxes[i]
            elif min_box > boxes[i]:
                min_box = boxes[i]

        # 문제의 조건, 가장 높은 박스와 가장 낮은 박스의 높이 차이가 1 이내면 break
        if 1 >= (max_box - min_box):
            break
        
        # index 메소드 사용했다가, 사용하지 않고 가장 높은 박스의 인덱스 -= 1, 가장 낮은 박스의 인덱스 += 1
        else:
            for j in range(len(boxes)):
                if boxes[j] == max_box:
                    boxes[j] -= 1
                    break

            for k in range(len(boxes)):
                if boxes[k] == min_box:
                    boxes[k] += 1
                    break
        
        # 박스를 한 번 옮겼으므로 dump -= 1 하고, 반복            
        dump -= 1

    print(f'#{tc} {max_box - min_box}')
