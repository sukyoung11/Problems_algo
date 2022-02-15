import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    N = len(numbers)

    for choice in range(2 ** N):
        # i => 선택한 요소의 인덱스를 상징하는 숫자
        subset = []

        # 스캐닝 시작
        for scanner in range(N):
            # 스캐닝 결과가 존재한다면,
            if choice & (1 << scanner):
                subset.append(numbers[scanner])

        if sum(subset) == 0:
            print(subset)
