import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dxs = [1, -1, 0, 0]
            dys = [0, 0, 1, -1]

            result = 0
            for idx in range(4):
                new_x = i + dxs[idx]
                new_y = j + dys[idx]
                if 0 <= new_x < N and 0 <= new_y < N:
                    diff = abs(matrix[i][j] - matrix[new_x][new_y])
                    result += diff



    print(f'{t+1} {result}')
