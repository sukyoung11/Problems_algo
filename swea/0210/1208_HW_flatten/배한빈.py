import sys
sys.stdin = open('input.txt')

# 1. 주석 (깔끔하게) 남기기
# 2. 변수명 읽는 사람이 이해하기 쉽게 잘 짜기
# 3. 함수화 도전하기

def solution(width, buildings):
    for idx in range(2, width-2):
        highest_building = max(buildings[idx - 2], buildings[idx - 1], buildings[idx + 1], buildings[idx + 2])

        if buildings[idx] > highest_building:
            return buildings[idx] - highest_building

T = 10
for tc in range(1, T+1):
    width = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0

    for idx in range(2, width - 2):
        cnt += solution(width, buildings)

    print(f'#{tc} {cnt}')
