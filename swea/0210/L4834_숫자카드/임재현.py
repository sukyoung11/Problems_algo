import sys

sys.stdin = open('input.txt')


def my_max(nums):
    max_value = 0
    for num in nums:
        if num >= max_value:
            max_value = num
    return max_value


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))
    counts = [0] * 10
    for card in cards:
        counts[card] += 1
    if counts.count(my_max(counts)) != 1:
        frequent_cards = []
        for card in cards:
            if counts[card] == my_max(counts):
                frequent_cards.append(card)
        print(f'#{tc} {my_max(frequent_cards)} {my_max(counts)}')
    else:
        print(f'#{tc} {counts.index(my_max(counts))} {my_max(counts)}')
