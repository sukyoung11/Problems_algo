import sys
sys.stdin = open("input.txt")

num_of_test = int(input())

for test in range(1, num_of_test+1):
    num_of_cards = int(input())

    cards = [int(i) for i in input()]
    counts = [0] * 10

    for card in cards:
        counts[card] += 1

    max_num = 0
    max_appear = counts[max_num]

    for i in range(1, 10):
        if counts[i] >= max_appear:
            max_num = i
            max_appear = counts[max_num]

    print(f'#{test} {max_num} {max_appear}')