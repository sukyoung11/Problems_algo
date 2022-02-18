import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
