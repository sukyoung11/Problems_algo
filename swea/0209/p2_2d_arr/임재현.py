import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())

# matrix = []
#
# for _in range(r):
#     row = list(map(int, input().split()))
#     matrix.append()
#
# print(matrix)

matrix = [list(map(int, input().split() for _ in range(r)))]

print(matrix)