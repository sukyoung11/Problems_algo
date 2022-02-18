import sys
sys.stdin = open('input.txt')

n = int(input())

nums = list(map(int, input().split()))

t = int(input())

for tc in range(1, t+1):
    row = list(map(int, input().split()))
    print(row)