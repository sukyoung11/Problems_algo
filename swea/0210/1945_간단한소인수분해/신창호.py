import sys
sys.stdin = open('input.txt')

factors = [2, 3, 5, 7, 11]
answer = [0] * 5

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    for _ in range(len(factors)):
        cnt = 0
        while N % factors[_] == 0:
            N = N // factors[_]
            cnt += 1
        answer[_] = cnt

    # answer(list to string)
    answer_str = " ".join(list(map(str, answer)))

    print(f'#{t}', answer_str)