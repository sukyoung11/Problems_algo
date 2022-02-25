import sys
sys.stdin = open('input.txt')

def dfs(maze,x,y):
    stack =[] # 방문 예정 리스트
    stack.append([x,y]) # 방문 예정 리스트에 추가
    maze[x][y] = 1  # 방문처리 => 1로 바꾸기

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if  0 <= nx < N and  0<= ny < N : # 범위 만족하고,
                if maze[nx][ny] == 3: # 3이면 리턴하고 종료
                    return 1

                elif maze[nx][ny] == 0: # 이동 가능하면(0이면) 방문 예정 리스트 추가
                    stack.append([nx,ny])  # 방문 예정 리스트 추가
                    maze[nx][ny] = 1 # 방문 처리
    return 0

# 1. 입력
T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

#2. 배열에서 2인 노드 찾아서 dfs()에 넣고 호출
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                print(dfs(maze,row,col))


