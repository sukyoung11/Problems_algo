import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    colors = [list(map(int,input().split())) for _ in range(N)]

# 0으로 채워진 matrix 만들기
    mat = []
    for i in range(10):
        mat_row = []
        for j in range(10):
            mat_row.append(0)
        mat.append(mat_row)

    for color in colors:
        if color[-1] == 1:  # 빨간색일 때 해당 위치에 +1
            for x in range(color[0],color[2]+1):
                for y in range(color[1], color[3]+1):
                    mat[x][y] += 1
        else:               # 파란색일 때 해당 위치에 +1
            for x in range(color[0],color[2]+1):
                for y in range(color[1], color[3]+1):
                    mat[x][y] += 1

    # 2(보라색)가 있으면 카운트
    cnt = 0
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 2:
                cnt+=1

    print(f'#{t} {cnt}')





