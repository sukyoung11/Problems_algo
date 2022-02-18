import sys
sys.stdin = open('input.txt')
# 총 한시간 반? 허공에 삽질만 한시간 20분한듯
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    N_list_A = [0] * N  # A, B를 각각 리스트화
    N_list_B = [0] * N
    for _ in range(N):
        A, B = list(map(int, input().split()))
        N_list_A[_] = A
        N_list_B[_] = B
    # print(N_list_A, N_list_B)
    P = int(input())

    C_list = [0] * P  # C 리스트화
    for _ in range(P):
        C = int(input())
        C_list[_] = C

    list_bus = [0] * (max(C_list)+1)  # 결과 리스트의 길이는 C 리스트 내 인자 중 가장 큰 값으로 결정
    # print(list_bus)
    for k in range(N): 
        for j in range(1, len(list_bus)):  # 결과 리스트 안에서 위치가 A와 B 사이에 위치한다면 1을 더해줌
            if N_list_A[k] <= j <= N_list_B[k]:
                list_bus[j] += 1
    # print(list_bus)
    result = []
    for C in C_list:  # 결과 리스트에서 C 위치의 인자만 빼서 새로 리스트를 만듬
        result.append(list_bus[C])
    # print(result)
    ans = ' '.join(list(map(str, result)))  # 출력값에 맞추어 전환
    print(f'#{tc} {ans}')