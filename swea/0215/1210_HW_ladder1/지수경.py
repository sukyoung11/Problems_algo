import sys
sys.stdin = open('input.txt')

for t in range(10):
    N = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    for i in range(0,100):
        row = 0
        col = i
        if ladder[row][i] == 1:
            while row < 99 :
                if col != 0 and ladder[row][col-1] == 1:
                    while ladder[row][col-1] != 0:
                        col -= 1
                        if col == 0:
                            break
                    row+=1

                elif col != 99 and ladder[row][col+1] == 1:
                    while ladder[row][col+1] != 0:
                        col += 1
                        if col == 99:
                            break
                    row+=1

                else:
                    row +=1

                position = ladder[row][col]

            if position == 2:
                print(f'#{t+1} {i}')
                break





