import sys
sys.stdin = open("input.txt")

def count(cards):
    counted = [0 for _ in range(10)]

    for card in cards:
        counted[card] += 1

    return counted

def check(counters):

    for i in range(8):
        if i <= 7 and counters[i] >= 1 and counters[i] == counters[i+1] and counters[i+1] == counters[i+2]:
            counters[i+1] -= counters[i]
            counters[i+2] -= counters[i]
            counters[i] -= counters[i]
        elif counters[i] == 6:
            counters[i] -= 6
        elif counters[i] >= 3:
            counters[i] -= 3
    
    for counter in counters:
        if counter != 0:
            return 'not baby-gin'
    else:
        return 'baby-gin'

num_of_games = int(input())

for game in range(1, num_of_games+1):
    cards = [int(char) for char in input()]
    
    result = check(count(cards))

    print(f'#{game} {result}')
