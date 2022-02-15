import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N,k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]

    result = 0
    for row in range(N):
        cnt = 0
        for col in range(N-1):
            if puzzle[row][col] == puzzle[row][col+1] ==1:
                cnt += 1
            else:
                if cnt == k-1:
                    result +=1
                cnt = 0
        if cnt == k-1:
            result += 1

    for col in range(N):
        cnt = 0
        for row in range(N-1):
            if puzzle[row][col] == puzzle[row+1][col] ==1:
                cnt += 1
            else:
                if cnt == k - 1:
                    result += 1
                cnt = 0
        if cnt == k - 1:
            result+=1

    print(f'#{t} {result}')

