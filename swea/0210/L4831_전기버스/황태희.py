import sys

sys.stdin = open('input.txt')


def bus_move(K, M, bus_stops):
    count = 0
    position = 0

    # 중단 조건: 남은 거리가 충전 없이도 주행 가능할 때
    while M - position > K:
        find = 0  # 주행 가능 거리 안에 충전소가 있니?

        # 주행 가능 거리 K를 역순으로 반복 ex) 3, 2, 1
        for move in range(K, 0, -1):

            # 해당 정류장에서 충전이 가능할 때,
            if bus_stops[position + move]:
                position += move  # 그 위치로 이동
                count += 1  # 충전 횟수 추가
                find = 1  # 충전 했습니다!
                break

        # 충전 못했니?
        if not find:
            return 0  # 그럼 넌 리턴 0이야

    return count  # 총 충전 횟수 리턴


T = int(input())

for tc in range(T):
    K, M, N = map(int, input().split())
    charge_stops = list(map(int, input().split()))
    bus_stops = [0 for _ in range(M + 1)]  # 마지막 인덱스가 M인 list 생성

    # 버스 정류장 지도 생성 ex)[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    for idx in charge_stops:
        bus_stops[idx] = 1

    # 정답 출력
    print(f'#{tc + 1} {bus_move(K, M, bus_stops)}')
