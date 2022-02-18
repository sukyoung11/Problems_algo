import sys
sys.stdin = open('input.txt')

def row_find(mat):
    for i in range(9):
            if len(set(mat[i]))!=9:
                return 0

    return 1

def col_find(mat):
        for i in range(9):
            col_list=[]
            for j in range(9):
                col_list.append(mat[j][i])
            if len(set(col_list)) != 9:
                return 0

        return 1

def sqr(mat):
    sqr_list = []
    for i in range(3):
        for j in range(3):
            for row in range(3*i,3*i+3):
               for col in range(3*j,3*j+3):
                   sqr_list.append(mat[row][col])
            if len(set(sqr_list)) != 9:
               return 0

    return 1

T = int(input())
for t in range(T):
    sudoku = [list(map(int,input().split())) for _ in range(9)]

    if row_find(sudoku):
        if col_find(sudoku):
            if sqr(sudoku):
                result = 1
            else:
                result = 0
        else:
            result = 0
    else:
        result = 0

    print(f'#{t+1} {result}')










