import sys
sys.stdin = open("input.txt")


def prime_power(n):
    primes = [2, 3, 5, 7, 11]
    power = []  # 답
    for prime in primes:
        # 지수의 갯수 구할 p
        p = 0
        while n % prime == 0:  # 나뉘면 (1이 되면 자동적으로 넘어가서 return으로 바로)
            # 소수의 갯수 세고
            p += 1
            # 나뉜 걸로 n을 다시 넣기
            n = n // prime
        # 끝나면 p를 답 list에 넣는다
        power.append(p)
    return power


T = int(input())

for tc in range(1, T+1):
    number = int(input())
    if 2 < number < 10000000:
        answer = prime_power(number)
        print(f'#{tc}', end=' ')
        print(*answer, sep=' ')
    else:
        print("숫자의 범위가 올바르지 않습니다.")
