import sys
sys.stdin = open('input.txt')


def my_max(nums):
    max_val = 0
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


def my_min(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


def my_index(nums, search):
    for idx, num in enumerate(nums):
        if num == search:
            return idx


for tc in range(1, 11):
    max_dump = cnt = int(input())
    boxes = list(map(int, input().split()))
    while cnt > 0:
        cnt -= 1
        max_value = my_max(boxes)
        max_index = my_index(boxes, max_value)
        min_value = my_min(boxes)
        min_index = my_index(boxes, min_value)
        boxes[max_index] -= 1
        boxes[min_index] += 1
        cha_ee = my_max(boxes) - my_min(boxes)
        if cha_ee == 1 or cha_ee == 0:
            print(f'#{tc} {cha_ee}')
    print(f'#{tc} {cha_ee}')


