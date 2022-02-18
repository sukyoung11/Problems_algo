import sys
sys.stdin = open("input.txt")

# 삼성시 버스 노선

def count_stop(num_of_stops, bus_lines, bus_stops): # 정류장 마다 지나치는 노선 수 계산
    result = [0] * num_of_stops # 정류장 마다 지나치는 노선 수(이 함수 결과값) 초기화

    for bus_line in bus_lines:
        for i in range(num_of_stops):
            result[i] += 1 if bus_line[0] <= bus_stops[i] <= bus_line[1] else 0
            # 버스 번호가 노선 범위 사이에 있으면 +1 아니면 +0

    return result


num_of_test = int(input())

for test in range(1, num_of_test+1):
    num_of_lines = int(input())
    bus_lines = [list(map(int, input().split())) for _ in range(num_of_lines)] # 버스 노선을 길이 2 리스트로 만들어서 전체 노선 리스트에 넣음

    num_of_stops = int(input())
    bus_stops = [int(input()) for _ in range(num_of_stops)]
    
    results = count_stop(num_of_stops, bus_lines, bus_stops) # 정류장 마다 지나치는 노선 수 계산하는 함수 호출

    print(f'#{test}', end='')
    for result in results:
        print(f' {result}', end='')
    print()