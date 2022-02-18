import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    # 구간합의 변화량을 기록할 리스트 changes를 생성한다. 최초값 0이 필요하다.
    changes = [0]
    for i in range(N - M):  # 구간의 총 갯수
        changes.append(changes[i] - a[i] + a[i + M])

    # changes 리스트에서 최댓값과 최솟값 탐색
    max = changes[0]
    min = changes[0]
    for m in range(len(changes)):
        if changes[m] > max:
            max = changes[m]
        elif changes[m] < min:
            min = changes[m]

    answer = max - min
    print(f'#{tc + 1} {answer}')