import sys
sys.stdin = open('input.txt')

# TC의 개수
T = int(input())

# 배열의 길이 \n 배열 받기
for tc in (1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    