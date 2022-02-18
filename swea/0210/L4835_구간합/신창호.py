import sys
sys.stdin = open('input.txt')

# T
# N M
# a1 a2 ... aN

tc = int(input())
for t in range(1, tc+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 부분합 리스트 만들기
    sum_arr = [0]*(N-M+1)
    for i in range(len(sum_arr)):
        for j in range(M):
            sum_arr[i] += arr[i+j]

    # max(부분합)-min(부분합)
    max_num = sum_arr[0]
    min_num = sum_arr[0]
    for k in range(1, len(sum_arr)):
        if sum_arr[k] > max_num:
            max_num = sum_arr[k]
        if sum_arr[k] < min_num:
            min_num = sum_arr[k]
    answer = max_num - min_num

    print(f'#{t} {answer}')
