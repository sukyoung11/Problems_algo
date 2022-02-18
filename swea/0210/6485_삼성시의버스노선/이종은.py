import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 각 bus_route 마다 start 부터 end 까지의 정류장을 지난다.
    # 각 bus_route 를 bus_routes 에 집어넣는다.
    bus_routes = []
    for _ in range(N):
        start, end = map(int, input().split())
        bus_route = [x for x in range(start, end+1)]
        bus_routes.extend(bus_route)

    # 지나야 되는 정류장 번호를 pass_stops 에 저장한다.
    pass_stops = [int(input()) for _ in range(int(input()))]

    # 지나야 되는 정류장 개수 만큼 cnt_routes 배열을 생성한다.
    cnt_routes = [0] * len(pass_stops)

    # 전체 버스 노선이 담긴 bus_routes를 순회하며
    # 지나야 되는 정류장 번호와 일치하면 cnt_routes 에 += 1
    for i in range(len(pass_stops)):
        for j in range(len(bus_routes)):
            if bus_routes[j] == pass_stops[i]:
                cnt_routes[i] += 1

    ans = " ".join(map(str, cnt_routes))
    print(f'#{tc} {ans}')


