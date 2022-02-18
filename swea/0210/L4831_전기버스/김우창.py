import sys
sys.stdin = open('input.txt')

T = int(input())
K, N, M = map(int, input().split())

cnt = 0
stop = []
for i in range(1, T+1):
    stop = list(map(int,input().split()))
    now_stop = 0
    for c in (N, 1, -1):

        if now_stop + K < stop:
            pass
        elif now_stop + K >= stop:
            now_stop += stop
            cnt += 1
            break
        elif c != stop:
            pass
조건
for문 돌려서 정류장 번호랑 다르면 패스
현재위치+K값보다 정류장 번호가 높으면 패스
현재위치+k값보다 정류장 번호가 낮은거 중에 최댓값 (거꾸로 돌리기)

1. 노선수 T , 1회 최대 이동 가능거리 K, 정류장 개수 N, 충전소 설치 개수 M
2. M값은 밑에 split 형태로 주어짐
