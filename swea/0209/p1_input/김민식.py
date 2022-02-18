import sys
sys.stdin = open('input.txt')

n = int(input())
print(n)

numbers = list(map(int, input().split()))
print(numbers)

T = int(input())
for tc in range(T):
    numbers = list(map(int, input().split()))
    print(numbers)