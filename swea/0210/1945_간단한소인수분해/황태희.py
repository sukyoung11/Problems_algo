import sys
sys.stdin = open('input.txt')

nums = [2, 3, 5, 7, 11]
N = int(input())

for count in range(N):
    print(f'#{count + 1}', end = '')
    target = int(input())
    for num in nums:
        answer = 0
        while not target % num:
            target /= num
            answer += 1
        print(f' {answer}', end = '')
    print('')