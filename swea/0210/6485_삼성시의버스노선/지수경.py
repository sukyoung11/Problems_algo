import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    bus_stations = []
    for n in range(N):
        A, B = list(map(int,input().split()))
        bus_stations.append(list(range(A, B+1)))
    P = int(input())

    stations = []
    for p in range(P):
        C = int(input())
        stations.append(C)


    result = []
    for station in stations:

        count = 0
        for bus_station in bus_stations:
           if station in bus_station:
            count+=1
        result.append(count)
    print(f'#{t} {" ".join(map(str,result))}')


