import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))

    for i in range(N-1,0,-1):
        for num in range(i):
            if nums[num] > nums[num+1]:
                nums[num], nums[num+1] = nums[num+1],nums[num]

    result=[]
    for i in range(5):
        result.append(nums[-(i+1)])
        result.append(nums[i])
    print(f'#{t} {" ".join(map(str,result))}')
