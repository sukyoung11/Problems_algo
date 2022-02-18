import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = input()
    count = []


    for i in range(10):
        cnt = 0
        for card in cards:
            if card == str(i):
                cnt +=1
        count.append(cnt)


    i_list =[]
    max_num = count[0]
    for i in range(1,len(count)):
        if count[i] >= max_num:
            max_num = count[i]
            i_list.append(i)


    print(f'#{t} {i_list[-1]} {max_num}')
