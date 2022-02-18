import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    box = list(map(int, input().split()))

    fall = [0] * n
    max_fall = 0
    for i in range(n - 1):
        for j in range(1, n):
            if box[i] > box[j]:
                fall[i] += 1
        if max_fall < fall[i]:
            max_fall = fall[i]

    print(max_fall)
