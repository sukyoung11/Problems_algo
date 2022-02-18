import sys
sys.stdin = open('input.txt')

T = int(input())

numbers = []
for tc in range(T):
    num = int(input())
    prime_cnt = [0] * 5

    while num != 1:
        if int(num / 11) == num / 11 and num / 11 > 0:
            prime_cnt[4] += 1
            num /= 11
            continue
        elif int(num / 7) == num / 7 and num / 7 > 0:
            prime_cnt[3] += 1
            num /= 7
            continue
        elif int(num / 5) == num / 5 and num / 5 > 0:
            prime_cnt[2] += 1
            num /= 5
            continue
        elif int(num / 3) == num / 3 and num / 3 > 0:
            prime_cnt[1] += 1
            num /= 3
            continue
        elif int(num / 2) == num / 2 and num / 2 > 0:
            prime_cnt[0] += 1
            num /= 2
            continue

    result = ' '.join(str(cnt) for cnt in prime_cnt)
    print(f'#{tc} {result}')
