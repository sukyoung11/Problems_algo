import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = []
    for i in range(N-M+1):
        sum_list.append(numbers[i:i+M])

    max_value = sum(sum_list[0])
    for i in range(len(sum_list)):
        if sum(sum_list[i]) >= max_value:
            max_value = sum(sum_list[i])

    min_value = sum(sum_list[0])
    for i in range(len(sum_list)):
        if sum(sum_list[i]) <= min_value:
            min_value = sum(sum_list[i])

    result = max_value - min_value

    print(f'#{tc} {result}')


