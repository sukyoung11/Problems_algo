import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int,input().split()))

    total = []
    i = 0
    while 0 <= i < N:
        max = price[i]
        for idx in range(i,N):
            if price[idx]>= max:
                max = price[idx]
                max_idx = idx

        buy = [max-num for num in price[i:max_idx]]
        total.append(sum(buy))

        i = max_idx+1
    print(f'#{t+1} {sum(total)}')




