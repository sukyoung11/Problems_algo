import sys
sys.stdin = open("input.txt")

#테스트케이스 받기
T = int(input())

#각 테스트 케이스별로 노선개수 N받기
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    # 버스노선별 시작정류장~마지막정류장을 각각 리스트로 받은 2차원 배열만들기
    for numbers in range(1, N+1):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    count_list = [0] * 5001
    for i in range(N):
        max = matrix[i][1]
        min = matrix[i][0]
        while (min <= max):
            count_list[min] += 1
            min += 1
    P = int(input())
    print(f'#{tc}', end=' ')
    for idx in range(P):
        if(idx < P-1):
            num = int(input())
            bus_stop = count_list[num]
            print(bus_stop, end=' ')
        else:
            num = int(input())
            bus_stop = count_list[num]
            print(bus_stop)