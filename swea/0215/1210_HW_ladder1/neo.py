import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 시작 좌표
    row, col = 99, matrix[99].index(2)

    while True:
        # 일단 위로 이동
        row -= 1

        # 좌회전 신호 확인
        if 0 <= col-1 < N and matrix[row][col-1]:
            # 좌회전 이후 직진
            while 0 <= col-1 < N and matrix[row][col-1]:
                col -= 1
        # 우회전 신호 확인
        elif 0 <= col+1 < N and matrix[row][col+1]:
            # 우회전 이후 직진
            while 0 <= col+1 < N and matrix[row][col+1]:
                col += 1
        
        # 시작 줄에 도달 했다면, 종료
        elif row == 0:
            break

    print(f'#{tc} {col}')
