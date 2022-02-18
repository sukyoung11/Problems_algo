import sys
sys.stdin = open("input.txt")

T = int(input())


def howManyBuses():
    # 자료 받기
    N = int(input())
    # 버스 노선을 list in list 형태로 받기
    passedStops = []
    for n in range(N):
        a, b = list(map(int, input().split()))
        passedStops.append(list(range(a, b+1)))

    P = int(input())
    # 버스 버정 번호 받기 + P 길이를 가진 answer 생성
    busStops = []
    answer = []
    for stops in range(P):
        busStops.append(int(input()))
        answer.append(0)

    # 계산
    for passed in passedStops:  # 지나간 버스 1개의 노선 * N개
        for i in passed:  # 그 버스가 지나간 정류장 하나씩 불러오기
            for idx, stop in enumerate(busStops):
                if i == stop:  # 묻는 정류장 번호 C와 같다면
                    answer[idx] = int(answer[idx]) + 1

    return answer


for tc in range(1, T+1):
    case = howManyBuses()
    print(f"#{tc}", end= " ")
    print(*case, sep=" ")
