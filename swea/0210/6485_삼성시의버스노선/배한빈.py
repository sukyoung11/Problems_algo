import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    bus_nosun = []
    for n in range(1, N+1):
        bus_nosun.append(list(map(int, input().split())))

    P = int(input())
    bus_stops_all = [0] * 5001

    C = []
    for p in range(P):
        C += list(map(int, input()))

    for c in C:
        for i in range(N):
            if bus_nosun[i][0] <= c <= bus_nosun[i][1]:
                bus_stops_all[c] += 1

    bus_stops = []
    for bus_stop in bus_stops_all:
        if bus_stop >= 1:
            bus_stops.append(str(bus_stop))

    result = ' '.join(bus_stops)

    print(f'#{tc} {result}')