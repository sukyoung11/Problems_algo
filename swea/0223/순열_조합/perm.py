
# numbers를 계속 바꿈.
def perm1(i):
    # base case(탐색중인 idx가 length와 같다 == 탐색 끝)
    if i == N:
        print(numbers)
        return

    # 제자리 그대로 부터, 마지막 idx까지
    for j in range(i, N):
        numbers[i], numbers[j] = numbers[j], numbers[i]
        perm1(i+1)
        numbers[i], numbers[j] = numbers[j], numbers[i]


numbers = [1, 2, 3]
N = len(numbers)

perm1(0)

# nPr r 가변
def perm2(i, k):
    # base case => DFS완전 탐색이 아닌, 탐색중 정지
    if i == k:
        print(*nums[:k])
    else:
        for j in range(i, N):
            nums[i], nums[j] = nums[j], nums[i]
            perm2(i+1, k)
            nums[i], nums[j] = nums[j], nums[i]


nums = [1, 2, 3, 4]
N = len(nums)
for i in range(1, N+1):
    perm2(0, i)

