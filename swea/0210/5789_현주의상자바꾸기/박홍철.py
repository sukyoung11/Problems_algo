import sys
sys.stdin = open("input.txt")

# 상자 바꾸기

num_of_test = int(input())

for test in range(1, num_of_test+1):
    num_of_boxes, num_of_trial = map(int, input().split())
    boxes = [0] * num_of_boxes # 박스 번호 초기화

    for changing_number in range(1, num_of_trial+1):
        box_left, box_right = map(int, input().split())
        for i in range(box_left-1, box_right): # list 특성상 왼쪽 번호 -1 에서 오른쪽 번호 -1 번째 원소에 숫자 달음
            boxes[i] = changing_number
        
    print(f'#{test}', end='')
    for box in boxes:
        print(f' {box}', end='')
    print()