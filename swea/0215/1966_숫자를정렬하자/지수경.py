import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))

    # 버블
    """
    for i in range(N-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    print(nums)
    """
    # 카운팅

    result = [0]*(N)
    count = [0]*(max(nums)+1)
    for i in range(N):
        count[nums[i]] += 1
    for i in range(len(count)-1):
        count[i+1]+=count[i]
    for i in range(len(nums)-1,-1,-1):
        count[nums[i]] -=1
        result[count[nums[i]]] = nums[i]

    print(result)


    # 선택
    """
    for i in range(N):
        min_num = nums[i]
        for num in range(i,N):
            if nums[num] < min_num:
                min_num = nums[num]
                nums[i],nums[num] = nums[num],nums[i]
    print(nums)
    """


