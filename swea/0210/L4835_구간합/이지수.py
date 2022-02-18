import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    New_list=[]
# 연속된 M개의 합 구하기
    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M):
            total += a[j]
        New_list.append(total)
# 최솟값, 최댓값 구하기
    max_value = 0
    min_value = 0
    for k in range(len(New_list)):
        if New_list[k] > max_value:
            max_value = New_list[k]
        elif New_list[k] < min_value:
            min_value = New_list[k]
        result = max_value - min_value
    print(f'#{tc} {result}')