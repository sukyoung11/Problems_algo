import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))


def fac(number):
    prime_numbers = [2, 3, 5, 7, 11]
    primes_result = [0] * 5
    for i in range(len(prime_numbers)):
        while number % prime_numbers[i] == 0:
            number = number // prime_numbers[i]
            primes_result[i] += 1
    return primes_result


for tc in range(N):
    result = (fac(numbers[tc]))
    print(f'#{tc + 1}', end=' ')
    for j in range(len(result)):
        print(result[j], end=' ')
    print()
