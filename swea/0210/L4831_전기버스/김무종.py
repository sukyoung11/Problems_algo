import sys

sys.stdin = open('input.txt')


def get_electronic_bus(charge_distance, total_distance, list_a):
    bus = 0
    cnt = 0
    while (bus + charge_distance) < total_distance:
        for go in range(charge_distance, 0, -1):
            if (bus + go) in list_a:
                bus += go
                cnt = cnt + 1
                break
        else:
            cnt = 0
            break
    return cnt

# 버스가 가는 거에 초점, 버스가 정류장을 이동 시에 충전거리 내에서 움직이는 것에 착안.
T = int(input())
for i in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    print(f'#{i}', get_electronic_bus(K, N, stations))
