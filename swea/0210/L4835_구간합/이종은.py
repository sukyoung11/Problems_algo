import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = sum(nums[0:M:])
    for i in range(len(nums)-M+1):
        M_nums = nums[i:i+M]
        sum_M_num = 0
        for j in M_nums:
            sum_M_num += j


        if sum_M_num > max_value:
            max_value = sum_M_num

        elif min_value > sum_M_num:
            min_value = sum_M_num

    print(f'#{tc} {max_value-min_value}')
