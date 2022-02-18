import sys
sys.stdin = open('input.txt')

r, c = list(map(int, input().split()))

matrix = []

# step 2
# for _ in range(r):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# print(matrix)

# step 3
matrix = [list(map(int, input().split())) for _ in range(r)]

print(matrix)