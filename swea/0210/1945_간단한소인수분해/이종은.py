import sys
sys.stdin = open('input.txt')

T = int(input())

# 문제에서 주어진 소수들의 리스트
sosus = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
    # N = 식을 진행할 숫자
    N = int(input())
    # sosus 각 숫자의 승의 수를 카운트하기 위해 arr 생성
    arr = [0, 0, 0, 0, 0]
    # 계속 나누면서 N이 1이 될 때까지
    while N != 1:
        # sosus의 각 소수 순회하기 위한 for문
        for sosu in range(len(sosus)):
            # 해당 소수가 N에 나누어 떨어지면
            if N%sosus[sosu] == 0:
                # arr에 해당 소수가 위치하는 인덱스에 += 1 카운트
                arr[sosu] += 1
                # N 은 해당 소수로 나눈 값으로 재할당 후 반복
                N /= sosus[sosu]

    print(f'#{tc}', end=' ')
    print(*arr, sep=' ')