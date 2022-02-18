import sys
sys.stdin = open("input.txt")

T = int(input())


def hj():
    N, Q = map(int, input().split())
    # 조건
    if Q > 10**3:
        print("Q가 너무 큽니다")
        return None

    # 박스 생성
    boxes = [0] * N

    # 한줄씩 받아오기
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for j in range(L-1, R):
            boxes[j] = i

    return boxes


for tc in range(1, T+1):
    answer = hj()
    print(f'#{tc}', end=' ')
    print(*answer, sep=' ')
