import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())

matrix = []

for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

print(matrix)
