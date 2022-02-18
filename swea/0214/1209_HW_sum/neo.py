import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for r_idx in range(N):
        row_sum = 0
        # 1개의 행 총합 구하기
        for c_idx in range(N):
            row_sum += matrix[r_idx][c_idx]
        if row_sum > max_sum:
            max_sum = row_sum

    for c_idx in range(N):
        col_sum = 0
        # 1개의 열 총합 구하기
        for r_idx in range(N):
            col_sum += matrix[r_idx][c_idx]

        if col_sum > max_sum:
            max_sum = col_sum

    sum_diagonal1 = 0
    sum_diagonal2 = 0

    for i in range(N):
        sum_diagonal1 += matrix[i][i]
        sum_diagonal2 += matrix[i][(N-1)-i]

    if sum_diagonal1 > max_sum:
        max_sum = sum_diagonal1

    if sum_diagonal2 > max_sum:
        max_sum = sum_diagonal2

    print(f'#{tc} {max_sum}')
