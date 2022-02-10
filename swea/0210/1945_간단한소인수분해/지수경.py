import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    nums = [2,3,5,7,11]
    result = [0, 0, 0, 0, 0 ]
    i = 0
    while i < 5:
        if N % nums[i] == 0:
            N = N // nums[i]
            result[i]+=1
        else:
            i += 1

    print(f'#{t} {" ".join(map(str,result))}')

