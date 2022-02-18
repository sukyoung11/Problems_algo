import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 정류장 수 K / 종점 정류장 N / 충전기 설치된 정류장 M
    K, N, M = map(int, input().split())

    # 충전소가 있는 위치
    charging_list = list(map(int, input().split()))
    charging_list.append(N)

    # 충전 횟수
    charging_count = 0
    # 남은 연료
    left_fuel = K + 1
    # 충전소 인덱스
    station_idx = 0

    for i in range(N):
        left_fuel -= 1

        # 충전소일 때
        if i in charging_list:

            # 마지막 충전소일 때, 종점까지 남은 연료가 있을 때
            if i == charging_list[-2] and left_fuel >= N - i:
                continue

            # 다음 충전소까지 남은 연료가 있을 때
            elif left_fuel >= charging_list[station_idx + 1] - i:
                station_idx += 1

            # 다음 충전소까지 남은 연료가 없을 때
            else:
                left_fuel = K
                charging_count += 1
                station_idx += 1

        # 충전소가 아닐 때
        else:
            # 종점이 아닌데 남은 연료가 없을 때
            if i != N and left_fuel == 0:
                charging_count = 0
                break

    print(f'#{tc} {charging_count}')
