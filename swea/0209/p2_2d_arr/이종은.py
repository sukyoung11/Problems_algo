import sys
sys.stdin = open('input.txt')

T, N = map(int, input().split())
print(T, N)

for _ in range(T):
    c = list(map(int, input().split()))
    print(c)
