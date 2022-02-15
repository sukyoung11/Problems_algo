import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())


    mat = [[0 for _ in range(N)] for _ in range(N)]
    x_move = [0, 1, 0, -1]
    y_move = [1, 0, -1, 0]

    x = y = 0
    idx = 0
    for i in range(1,N**2+1):
        mat[x][y] = i
        x += x_move[idx]
        y += y_move[idx]

        if not (0 <= x < N) or not (0 <= y < N) or mat[x][y] != 0:
            x -= x_move[idx]
            y -= y_move[idx]

            idx = (idx+1)%4
            x += x_move[idx]
            y += y_move[idx]

    print(f'#{t} ')
    for i in range(N):
        for j in range(N):
            print(mat[i][j],end='')
        print('')











