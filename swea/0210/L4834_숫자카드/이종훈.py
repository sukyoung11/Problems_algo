import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    nums = input()
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#    arr = [0 for _ in range(10)]
    for i in nums:
        arr[int(i)] += 1

    max_num = 0
    max_0 = 0

    for j in range(len(arr)):

        if arr[j] >= max_0:  # >=처리를 통해 더 높은 카드를 채택할 수 있다.
            max_num = j  # 카드 넘버
            max_0 = arr[j]  # 같은 숫자가 나온 횟수

    print("#%d %d %d" % (tc, max_num, max_0))  # tc와 max_num, max_0
