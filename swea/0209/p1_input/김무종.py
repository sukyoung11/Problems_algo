import sys
sys.stdin = open('input.txt')

a = int(input())
list1 = list(map(int, input().split()))
n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    print(a, list1, x, y, z)