import sys
sys.stdin =open("input.txt")

test = int(input())

for t in range(1, test+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    answer = [numbers[0], numbers[0]]
    for i in range(1, N):
        if numbers[i] > answer[0]:
            answer[0] = numbers[i]
        if numbers[i] < answer[1]:
            answer[1] = numbers[i]

    print(f'#{t} {answer[0]-answer[1]}')
