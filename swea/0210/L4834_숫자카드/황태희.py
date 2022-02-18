import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    number = int(input())
    cards = []
    for _ in range(N):
        cards.append(number % 10)
        number = number // 10

    card_set = list(set(cards))


    how_many = [0 for _ in range(len(card_set))]

    for idx in range(len(card_set)):
        for card in cards:
            if card_set[idx] == card:
                how_many[idx] += 1

    my_max = 0
    max_num = 0

    for i in range(len(how_many)):
        if how_many[i] > my_max:
            my_max = how_many[i]
            max_num = card_set[i]
        elif how_many[i] == my_max:
            if card_set[i] > max_num:
                max_num = card_set[i]

    print(f'#{tc + 1} {max_num} {my_max}')