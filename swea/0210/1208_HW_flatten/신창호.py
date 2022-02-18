import sys

sys.stdin = open('input.txt')

# 10번 시행 고정

# idea 1
# min max 찾아서 각각 +1 -1 해주고
# 덤프 횟수만큼 시행
# max-min

# idea 2
# max와 next_max찾아서 빼주고 개수 곱함
# 누적곱이 dump를 넘는순간 max값 출력
# min과 next_min 찾아서 빼주고 개수를 곱함
# 누적곱이 덤프를 넘는 순간 min 출력
# max- min

# idea 1

def flatten(list1):
    my_max1 = list1[0]
    idx = 0
    for i in range(1, len(list1)):
        if list1[i] > my_max1:
            my_max1 = list1[i]
            idx = i
    list1[idx] -= 1

    my_min1 = list1[0]
    idx = 0
    for i in range(1, len(list1)):
        if list1[i] < my_min1:
            my_min1 = list1[i]
            idx = i
    list1[idx] += 1


for t in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))

    for _ in range(dump):
        flatten(box_list)

    my_max = box_list[0]
    my_min = box_list[0]
    for _ in range(1, len(box_list)):
        if box_list[_] > my_max:
            my_max = box_list[_]
        if box_list[_] < my_min:
            my_min = box_list[_]

    answer = my_max - my_min
    print(f'#{t} {answer}')
