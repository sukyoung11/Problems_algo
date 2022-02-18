import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    box_list = list(map(int, input().split()))
    new_list = [0] * len(box_list)

    for i in range(len(box_list)):
        cnt = 0
        for j in range(i+1, len(box_list)):
            if box_list[i] <= box_list[j]:
                cnt += 1
        new_list[i] = N-i-1-cnt

    answer = new_list[0]
    for j in new_list[1:]:
        if answer < j:
            answer = j

    print(answer)