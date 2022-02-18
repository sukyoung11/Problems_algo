import sys
sys.stdin = open('input.txt')

n = int(input())

numbers = list(map(int, input().split()))

T = int(input())

by_3 = []

for _ in range(3):
    by_3.append(list(map(int, input().split())))