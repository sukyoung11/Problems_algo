import sys
sys.stdin = open("input.txt")

num_of_test = int(input())

for test in range(1, num_of_test+1):
    num_of_nums, length = map(int, input().split())

    numbers = [int(i) for i in input().split()]

    min = 0

    for i in range(length):
        min += numbers[i]

    max = min

    for i in range(1, num_of_nums-length+1):
        len_sum = 0
        for j in range(length):
            len_sum += numbers[i+j]
        min = len_sum if len_sum < min else min
        max = len_sum if len_sum > max else max
    
    print(f'#{test} {max-min}')
