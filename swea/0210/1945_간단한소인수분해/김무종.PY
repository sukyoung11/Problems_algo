import sys
sys.stdin = open('input.txt')
# 함수 이름은 동사로
def get_prime(n):
    numbers = [2, 3, 5, 7, 11]
    primes = [0]*5
    while True:
        if n == 1:
            break
        elif n % numbers[0] == 0:
            n = n // 2
            primes[0] += 1
            continue
        elif n % numbers[1] == 0:
            n = n // 3
            primes[1] += 1
            continue
        elif n % numbers[2] == 0:
            n = n // 5
            primes[2] += 1
            continue
        elif n % numbers[3] == 0:
            n = n // 7
            primes[3] += 1
            continue
        elif n % numbers[4] == 0:
            n = n // 11
            primes[4] += 1
            continue

    return ' '.join(map(str, primes))


T = int(input())
for i in range(1, T+1):
    number = int(input())
    print(f'#{i} {get_prime(number)}')

