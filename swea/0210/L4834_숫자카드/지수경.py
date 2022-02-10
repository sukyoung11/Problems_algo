import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int,input().split()))
    count = []

    for i in range(10):
        cnt = 0
        for card in cards:
            if card == i:
                cnt +=1
        count.append(cnt)

    max_num = count[0]
    for i in range(1,len(count)):
        if count[i] >= max_num:
            max_num = count[i]

    print(i,max_num)
