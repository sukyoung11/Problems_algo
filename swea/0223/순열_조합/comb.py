"""
from itertools import permutations
from itertools import combinations

numbers = [1, 2, 3, 4]

# numbers P 4
for perm in permutations(numbers, 4):
    print(perm)

# numbers P n
for perm in permutations(numbers, n):
    print(perm)


from itertools import combinations

numbers = [1, 2, 3, 4]

for i in range(1, len(numbers)+1):
    for comb in combinations(numbers, i):
        print(comb)

"""
# 조합 => n C r => r 가변
def comb(check_idx, start):
    """
    check_idx: check[n] 에서 채울 idx
    :param start: 선택 구간의 시작점
    """

    # 재귀 탈출 base case(다 골랐다면)
    if check_idx == r:
        print(check)
    else:
        """
        s => 남겨진 구간의 시작 idx(재귀 호출마 1씩 올림)
        N-r => 전체 - 고를 조합 수
        N-r+check_idx => N
        
        """
        end = N-r+check_idx
        for i in range(start, end+1):
            check[check_idx] = i
            comb(check_idx+1, i+1)


numbers = [1, 2, 3, 4, 5]
N = len(numbers)

for r in range(1, N+1):
    check = [None] * r
    # for r in range(1, 6):
    comb(0, 0)
