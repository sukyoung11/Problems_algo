import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for numbers in range(1, N+1):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)
    max_value = 0
    for i in range(N):
        if matrix[i][-1] > max_value:
            max_value = matrix[i][-1]
    count_list = [0] * (max_value + 1)
    for i in range(N):
        max = matrix[i][1]
        min = matrix[i][0]
        while (min <= max):
            count_list[min] += 1
            min += 1
    P = int(input())
    print(f'#{tc}', end=' ')

    for _ in range(P):
        num = int(input())
        bus_stop = count_list[num]
        if count_list[num] == count_list[-1]:
            print(bus_stop)
        else:
            print(bus_stop, end = ' ')


