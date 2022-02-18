import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    answer = list()

    for mod in [2, 3, 5, 7, 11]:
        exp = 0     # 지수
        while not N % mod:  # N이 각각의 소수로 나누어 떨어지지 않게 될 때까지 반복
            exp += 1
            N /= mod
        answer.append(exp)

    answer = ''.join(list(map(str, answer)))
    print(f'#{tc + 1} {answer}')
