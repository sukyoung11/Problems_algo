import sys
sys.stdin = open('input.txt')

def dfs(maze,x,y):
    maze[x][y] = 1 # 방문처리 => 1로 바꾸기

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if  0 <= nx < N and  0<= ny < N : # 범위 만족
            if maze[nx][ny] != 1:
                dfs(maze,nx,ny)

# 1. 입력

T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

#2. 배열에서 2인 노드 찾아서 dfs()에 넣고 호출

    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:  # 출발지점
                dfs(maze,row,col)
            if maze[row][col] == 3: # 도착지점
                goal_x = row
                goal_y = col

#3. 3에 도착했는지 판별

    if maze[goal_x][goal_y] == 1:
        answer = 1
    else:
        answer = 0

    print(f'#{t+1} {answer}')
