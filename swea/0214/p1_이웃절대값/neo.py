import sys
sys.stdin = open('input.txt')

T = int(input())


def get_around_sum(row, col):
    dx = [-1, 1, 0, 0]  # v
    dy = [0, 0, -1, 1]  # v

    center = matrix[row][col]
    abs_sum = 0
    for d in range(4):  # v
        new_row, new_col = row + dx[d], col + dy[d]  # v

        # matrix 인덱스 접근 전에 미리 index 체크!
        if 0 <= new_row < N and 0 <= new_col < N:  # v
            near = matrix[new_row][new_col]  # v
            abs_sum += abs(center - near)

    return abs_sum


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for row in range(0, N):
        for col in range(0, N):
            total += get_around_sum(row, col)

    print(f'#{tc} {total}')




