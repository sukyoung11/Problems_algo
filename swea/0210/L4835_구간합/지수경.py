import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N, M = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    # M개씩 더한 리스트 만들기
    sum_list = []
    for i in range(N-M+1):
        ans = 0
        for j in range(i,i+ M):
           ans += nums[j]
        sum_list.append(ans)

    # 최대값, 최소값 구하기
    max_num = min_num = sum_list[0]
    for num in range(1,len(sum_list)):
        if sum_list[num] >= max_num:
            max_num = sum_list[num]
        if sum_list[num] <= min_num:
            min_num = sum_list[num]

    result = max_num - min_num
    print(f'#{t} {result}')







