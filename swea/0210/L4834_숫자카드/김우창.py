import sys
sys.stdin = open('input.txt')
# 테스트 케이스 개수 T
T = int(input())
for tc in range(1, T+1):
    # 카드 장수 N
    N = int(input())
    # 0부터 9까지 숫자 배열
    arr = [0]*10
    # arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 얘랑 같은 말

    # N개의 숫자 ai 여백없이
    # 0으로 시작할 수도 있어서 int 안 주고 시작
    ai = input()

    # for문 돌때마다 arr에 ai의 숫자 1개씩 투입
    for i in range(len(ai)):
        arr[int(ai[i])] += 1

    # 가장 많은 카드 숫자 max_num
    max_num = 0
    # 가장 많은 카드의 장수 max_count
    max_count = 0
    for j in range(len(arr)):
        if arr[j] >= max_count:
            max_num = j
            max_count = arr[j]

    print(f'#{tc} {max_num} {max_count}')


# for문을 2개 같이 돌림
# 하나는 입력된 숫자 ai 의 카운트를 arr에 하나씩 올리는 for문
# 하나는 arr의 최댓값 숫자 == 가장 많은 카드의 숫자번호, 장 수