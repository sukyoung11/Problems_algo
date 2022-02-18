import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    new_mat90 = [[0] * N for _ in range(N)]
    new_mat180 = [[0] * N for _ in range(N)]
    new_mat270 = [[0] * N for _ in range(N)]

    # 90
    for i in range (N):
        for j in range(N):
            new_mat90[j][N-i-1] = mat[i][j]


    #180
    for i in range(N):
        new_mat180[N-i-1] = mat[i][::-1]


    #270
    for i in range(N):
        for j in range(N):
           new_mat270[j][i] = mat[i][N-j-1]

    print(f'#{t+1}')
    for i in range(N):
        print(''.join(list(map(str,new_mat90[i]))),''.join(list(map(str,new_mat180[i]))),''.join(list(map(str,new_mat270[i]))))



