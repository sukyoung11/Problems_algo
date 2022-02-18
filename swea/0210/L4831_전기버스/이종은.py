import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    # 버스가 수용 가능한 기름게이지, 총거리, 충전소개수
    K, N, M = map(int, input().split())

    # 충전소 있는 장소 [4, 7, 9, 14, 17]
    charge = list(map(int, input().split()))

    bus = 0
    present_K = K
    charge_cnt = 0
    stop_num = 0

    # 버스가 종점에 도착할 때 까지
    while bus != N:

        # 현재 기름칸이 0 이하면, 0 출력하고 중단
        if 0 >= present_K:
            charge_cnt = 0
            break

        # 버스 한칸 이동, 기름 한칸 감소
        bus += 1
        present_K -= 1

        # 버스가 충전소 있는 장소에 도착하면
        if bus in charge:
            # 충전소 넘버 += 1
            stop_num += 1

            # 마지막 충전소에 도착하면
            if stop_num == len(charge):
                # 종점까지 남은 거리(총거리 - 버스현위치)가 현재 기름칸보다 많이 들면
                if N - bus > present_K:
                    # 충전하자
                    charge_cnt += 1
                    present_K = K

                # 현재 기름칸으로 종점까지 갈 수 있다면 pass
                else:
                    pass

            elif charge[stop_num] - bus > present_K:
                charge_cnt += 1
                present_K = K

    print(f'#{i} {charge_cnt}')