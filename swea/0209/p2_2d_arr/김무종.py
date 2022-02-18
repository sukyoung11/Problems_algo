import sys
sys.stdin = open('input.txt')

row, col = map(int, input().split())
list1 = []
for i in range(row):
    list1.append(list(map(int, input().split())))
print(list1)