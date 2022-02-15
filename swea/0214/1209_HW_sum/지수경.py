import sys
sys.stdin = open('input.txt')

for t in range(10):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]

    result_dg = result_dg_reverse = 0
    result=[]
    for i in range(100):
        result_dg+=matrix[i][i]
        result_dg_reverse += matrix[i][100-i-1]
        result_row = result_col = 0

        for j in range(100):
            result_row += matrix[i][j]
            result_col += matrix[j][i]
        result.append(result_row)
        result.append(result_col)
    result.append(result_dg)
    result.append(result_dg_reverse)

    print(f'#{N} {max(result)}')