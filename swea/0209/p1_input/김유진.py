import sys
sys.stdin = open("input.txt")

N = int(input())
numbers = list(map(int, input().split()))

T = int(input())

for tc in range(1, T+1):
    row = list(map(int, input().split()))
    print(row)