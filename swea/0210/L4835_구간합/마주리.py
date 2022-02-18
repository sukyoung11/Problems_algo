import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    # 최대값, 최소값 초기화
    max_sum = min_sum = 0
    for i in range(M):
        max_sum += numbers[i]
        min_sum += numbers[i]

    # 최대값, 최소값 구하기
    for i in range(N - M + 1):
        tmp_sum = 0
        for j in range(M):
            tmp_sum += numbers[i + j]

        if tmp_sum > max_sum:
            max_sum = tmp_sum
        elif tmp_sum < min_sum:
            min_sum = tmp_sum

    print(f'#{tc} {max_sum - min_sum}')
