import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    N = len(numbers)

    for i in range(1, N+1):
        subset = list(combinations(numbers, i))
        for sets in subset:
            if sum(sets) == 0:
                print(sets)



