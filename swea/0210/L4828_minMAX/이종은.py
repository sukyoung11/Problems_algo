import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[0]
    min_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
        elif min_value > num:
            min_value = num
    print(f'#{tc} {max_value-min_value}')