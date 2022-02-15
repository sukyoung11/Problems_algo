import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    M,N = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(M)]

    result_sum=[]
    for i in range(M-N+1):
        for j in range(M-N+1):
            result = 0
            for row in range(i,i+N):
                for col in range(j,j+N):
                    result += mat[row][col]

            result_sum.append(result)


    # print(f'#{t} {max(result_sum)}')

    max_num = result_sum[0]
    for i in range(1,len(result_sum)):
        if result_sum[i] > max_num:
            max_num = result_sum[i]
    print(f'#{t} {max_num}')