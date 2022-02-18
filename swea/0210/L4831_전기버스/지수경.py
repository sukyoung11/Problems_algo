import sys
sys.stdin = open('input.txt')

t = int(input())
for i in range(1, t + 1):

    k, n, m = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    cnt = 0
    now = 0  # 버스의 현재 위치

#여기서부터 코드!
    while now < n - k:
        drive = list(range(now + 1, now + k + 1))  # 버스가 현재 위치로부터 주행 가능한 구간(drive)
        chargers = [charger for charger in drive if charger in stations]  # drive와 충전기 위치 리스트(stations)와의 교집합

        if chargers == []:  # 구간에 충전기가 없을 경우 0
            cnt = 0
            break

        else:  # 충전기가 있는 경우
            now = chargers[-1]  # 충전 가능한 곳(chargers) 중 최대한 멀리서 충전, 현재 위치 이동
            cnt += 1

    print(f'#{i} {cnt}')
