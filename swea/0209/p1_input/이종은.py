import sys
sys.stdin = open('input.txt')

a = int(input())
print(a)

b = list(map(int, input().split()))
print(b)

c = int(input())
print(c)

for _ in range(c):
    d = list(map(int, input().split()))
    print(d)








# n = int(input())
# print(n)
# numbers = list(map(int, input().split()))
# print(numbers)
#
# T = int(input())
# print(T)
#
# for tc in range(1, T+1):
#     row = list(map(int, input().split()))
#     print(row)