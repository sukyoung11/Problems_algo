import sys
sys.stdin = open('input.txt')
# 50분
T = int(input())

for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # 인자가 0인 리스트를 길이 N으로 생성
    line = [0] * N
    line_number = list(map(int, input().split()))
    # 주유소가 있는 인덱스의 값을 1로 만들기
    for number in line_number:
        line[number] += 1

    j = 0
    result = 0
    # j는 현 위치, result는 충전 횟수
    # 정류장 번호가 N 보다 작을 때,
    while j < N:
        # 정류장 번호 j에서 최대 도달 거리인 K만큼 이동한 지점부터 앞으로 돌아온 거리(x) = j+K-x
        for x in range(K):
            # j+k-x가 N보다 작다면
            # 위치 j를 변경하고 값을 출력
            if j+K-x >= N:
                j += (K-x)
                print(f'#{tc} {result}')
                break
            # 가장 멀리 도달할 수 있는 주유소를 찾아 충전하고 횟수+1
            # 위치 j 변경
            elif line[j+K-x] == 1:
                j += (K-x)
                result += 1
                break
            # 만약 최대 도달 거리 K까지 주유소가 없다면 0을 출력
            elif x == K-1 and line[j+K-x] == 0:
                j += N
                print(f'#{tc} 0')

