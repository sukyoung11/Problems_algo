import sys
sys.stdin = open('input.txt', encoding='utf-8')

def row_find(mat,matby,word):
    for i in range(matby):
        for j in range(matby-word+1):
            test = mat[i][j:j+word]
            if test == test[::-1]:
                return test
    return 0

def col_find(mat,matby,word):
    for i in range(matby):
        for j in range(matby-word+1):
            result = []
            for col in range(j,j+word):
                result.append(mat[col][i])
            if result == result[::-1]:
                return "".join(result)



T = int(input())
for t in range(T):
    M, N = list(map(int,input().split()))
    letters = [input() for _ in range(M)]

    if row_find(letters,M,N) == 0:
        print(f'#{t+1} {col_find(letters,M,N)}')
    else:
        print(f'#{t+1} {row_find(letters,M,N)}')






