import sys
from collections import deque
sys.stdin = open('input.txt')

for t in range(10):
    N = int(input())
    numbers = deque(map(int,input().split()))
    while 1:
        for i in range(1,6):
            num = numbers.popleft()
            num = num-i
            if num <= 0:
                numbers.append(0)
                break
            else:
                numbers.append(num)
        if num <= 0:
            break
    print(f'#{N} {" ".join(map(str,numbers))}')