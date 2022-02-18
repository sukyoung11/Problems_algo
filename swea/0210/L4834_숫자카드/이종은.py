import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()

    compare_card = [0] * N

    for card in range(len(cards)):
        compare_card[card] += cards.count(cards[card])

    max_card_cnt = compare_card[0]

    for i in range(len(compare_card)):
        if compare_card[i] > max_card_cnt:
            max_card_cnt = compare_card[i]

    max_cards = []

    for j in range(len(cards)):
        if cards.count(cards[j]) == max_card_cnt:
            max_cards.append(int(cards[j]))

    max_card = max_cards[0]
    for k in range(len(max_cards)):
        if max_cards[k] > max_card:
            max_card = max_cards[k]

    print(f'#{tc} {max_card} {max_card_cnt}')
