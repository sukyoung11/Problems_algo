import sys
sys.stdin = open('input.txt')

def get_max_min(total, area, list_a):
    max_area = min_area = 0
    for num in range(0, area):
        max_area = max_area + list_a[num]
        min_area = min_area + list_a[num]
    for j in range(total-area+1):
        tmp = 0
        for k in range(j+area-1, j-1, -1):
            tmp += list_a[k]
        if tmp > max_area :
            max_area = tmp
        if tmp < min_area:
            min_area = tmp
    return max_area-min_area


T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(f'#{i}', get_max_min(N, M, numbers))


