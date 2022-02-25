"""
from itertools import permutations
numbers = [1,2,3,4]
print(list(permutations(numbers)))
"""


def comb(idx):
    if idx == N:
        return print(result)

    result[idx] = True
    comb(idx+1)
    result[idx] = False
    comb(idx+1)

T = int(input())

for t in range(T):
    numbers = list(map(int,input().split()))
    numbers = [1,2,3]
    N = len(numbers)
    result = [None] * N
    comb(0)


