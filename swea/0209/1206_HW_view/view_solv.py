import sys
sys.stdin = open('input.txt')

# T = 10
# for tc in range(1, T+1):
#     width = int(input())
#     buildings = list(map(int, input().split()))
#     tnt = 0
#
#     for idx in range(2, width-2):
#         highest_building = max(buildings[idx-1], buildings[idx+1], buildings[idx+2])
#         if buildings[idx] > highest_buildings:
#             cnt += buildings[idx] - highest_building
#
#     print(f'#{tc} {cnt}')


# sol 2 함수화 하기
def solution(buildings):
    # 현재 확dls하고자 하는 빌딩 제외 +-2 빌딩들 중 가장 높은 빌딩 찾기
    highest_building = max(buildings[idx - 1], buildings[idx + 1], buildings[idx + 2])

        # 현재 확인하는 빌딩이 가장 높다면,
        if buildings[idx] > highest_buildings:
            # 조망 가능한 층수를 return
            return buildings[idx] - highest_building

T = 0
for tc in range(1, T + 1):
    width = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0

    for idx in range(2, width - 2):
            cnt += solution(width, buildings)

    print(f'#{tc} {cnt}')

# 1. 주석(깔끔하게) 남기기
# 2. 변수명 읽는 사람이 이해하기 쉽게 잘 짜기
# 3. 함수화 도전하기-남들이 봤을 때 핵심 로직이 어딘지 알 수 있다.