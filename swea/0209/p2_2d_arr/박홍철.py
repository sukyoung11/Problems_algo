import sys
sys.stdin = open("input.txt")

r, c = list(map(int, input().split()))

matrix = [ list(map(int, input().split())) for _ in range(r)]

print(matrix)
