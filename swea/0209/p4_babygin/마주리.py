import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str_num = list(map(str, input()))
    int_num = [int(num) for num in str_num]

    count = [0] * 10

    for i in int_num:
        count[i - 1] += 1

    i = tri = run = 0

    while i < 10:
        # triplet 조사
        if count[i] >= 3:
            count[i] -= 3
            tri += 1
            continue

        # Run 조사
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
    print()
