import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N=상자개수, Q=상자에 넘버링 작업할 횟수
    N, Q = map(int, input().split())
    # N개수 만큼 배열 생성 (상자 진열)
    arr = [0] * N
    # for문으로 작업 횟수 순회
    for qc in range(Q):
        # L번째 상자부터 R번째 상자까지
        L, R = map(int, input().split())
        # arr 인덱스넘버에 맞춰 L-1, R
        for i in range(L-1, R):
            # arr에 L-1부터 R까지 작업횟수번째 넘버 기입
            arr[i] = qc+1

    print(f'#{tc}', end=' ')
    print(*arr, sep=' ')
