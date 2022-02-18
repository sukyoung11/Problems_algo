import sys

sys.stdin = open('input.txt')


def is_triplet():
    for number in range(10):
        if card_count[number] >= 3:
            card_count[number] -= 3


def is_run():
    for number in range(10):
        if card_count[number] > 0 and card_count[number + 1] > 0 and card_count[number + 2] > 0:
            for k in range(3):
                card_count[number + k] -= 1
            return


tc = int(input())
for t in range(1, tc + 1):
    card_count = [0] * 10
    for card in map(int, list(input())):
        card_count[card] += 1

    # triplet 탐색
    is_triplet()
    is_triplet()

    # run 탐색
    is_run()
    is_run()

    if card_count == [0] * 10:
        print('Baby Gin')
    else:
        print('Lose')