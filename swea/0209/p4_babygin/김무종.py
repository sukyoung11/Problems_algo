import sys
sys.stdin = open('input.txt')
T = int(input())
for _ in range(1, T + 1):
    numbers = list(map(int, input()))
    count = [0] * 10

    for num in numbers:
        count[num - 1] += 1

    i = tri = run = 0

    while i < 10:
        if count[i] >= 3:
            count[i] -= 3
            tri += 1
            continue

        if i < 8 and count[i] >= 1 and count[i + 1] >= 1 and count[i + 2] >= 1:
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
            run += 1
            continue

        i += 1

    if run + tri == 2:
        print("Baby Gin")
    else:
        print("Lose")
