import sys
sys.stdin = open("input.txt")

num_of_drive = int(input())

for drive in range(1, num_of_drive+1):
    num_of_Go, num_of_stops, num_of_charings = map(int, input().split())
    charging_stop = [int(i) for i in input().split()]

    result = 0 # 충전 횟수(결과값)
    position = 0 # 버스 위치

    while position < num_of_stops:
        for i in range(position + num_of_Go, position, -1): # 가능한 멀리 있는 충전소 이용을 위해 도달할 수 있는 정거장 중 가장 먼 곳부터 탐색
            if i in charging_stop: # 탐색 중 충전소를 찾음 -> 횟수 추가, 버스 위치 갱신
                position = i
                result += 1
                break
            elif i >= num_of_stops: # 탐색 중 마지막 정류소를 지나침 -> 버스 위치만 갱신
                position = i
                break
        else: # break로 for 탈출 못함 == 탐색 결과 갈 곳이 없음 == 끝
            result = 0
            break

        
    print(f'#{drive} {result}')