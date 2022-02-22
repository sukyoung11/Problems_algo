import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    # 0으로 채워진 빈 리스트
    mat = []
    for i in range(N):
            mat.append([0]*(i+1))

    # 파스칼의 삼각형
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i: # 양 끝은 1
                mat[i][j]=1
            else:
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]


    #출력
    print(f'#{t+1}')
    for row in range(N):
        for col in range(row+1):
            print(mat[row][col],end=' ')
        print()


