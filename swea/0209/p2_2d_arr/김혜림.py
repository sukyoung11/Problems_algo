import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())

matrix = []
# 
# # step 1
# for _ in range(r):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# 
# # step 2
# for _ in range(r):
#     matrix.append(list(map(int, input().split())))
#     
# step 3
matrix = [list(map(int, input().split())) for _ in range(r)]

print(matrix)
