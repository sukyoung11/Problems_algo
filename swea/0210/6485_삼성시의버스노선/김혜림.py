import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 버스 노선은 2차원 리스트, 버스 정류장은 1차원 리스트로 받는다.
    N = int(input())
    bus_routes = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stops = []
    for _ in range(P):
        bus_stops.append(int(input()))
    
    # 노선별로 지나는 정류장 번호(bus_stop)를 인덱스로 받아 지나는 횟수를 counts에 누적한다.
    counts = [0]*5001
    for bus_route in bus_routes:
        for no in range(bus_route[0], bus_route[1]+1):
            counts[no] += 1
    
    # 출력: P에서 제시한 정류장 번호(bus_stop)를 인덱스로 받아 스페이스 한칸을 텀으로 두고 프린트한다.
    print(f'#{tc}', end=' ')
    for bus_stop in bus_stops:
        if bus_stop == bus_stops[-1]:
            print(counts[bus_stop])
            continue
        print(counts[bus_stop], end=' ')
        
    