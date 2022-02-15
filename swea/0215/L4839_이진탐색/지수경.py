import sys
sys.stdin = open('input.txt')

def seach_page(book, target):
    l = 1
    r = book
    cnt = 0
    while l <= r:
        mid = (r + l) // 2
        if mid == target:
            return cnt
        elif mid > target:
            r = mid
            cnt += 1
        else:
            l = mid
            cnt += 1
    return 1000000  # 책에 원하는 페이지가 없는 경우 매우 큰 값을 리턴

T = int(input())
for t in range(1,T+1):
    p,pa,pb = list(map(int,input().split()))
    A_cnt = seach_page(p, pa)
    B_cnt = seach_page(p, pb)

    if A_cnt > B_cnt :
        winner = 'B'
    elif A_cnt == B_cnt:
        winner = 0
    else:
        winner = 'A'

    print(f'#{t} {winner}')