import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    primes = [2, 3, 5, 7, 11]
    counts = [0] * 12
    
    for prime in primes:
        while N % prime == 0:
            N = N // prime
            counts[prime] += 1
    
    print(f'#{tc} ', end='')
    for prime in primes:
        if prime == 11:
            print(counts[prime])
            continue
        print(counts[prime], end=' ')