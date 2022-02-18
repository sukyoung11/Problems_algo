import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = [0] * (N-M+1)
    for i in range(N-M+1):
        K = M
        while K >= 1:
            b[i] += (a[i+K-1])
            K -= 1

    max_b = min_b = b[0]
    for elem in b:
        if elem > max_b:
            max_b = elem
        if elem < min_b:
            min_b = elem

    print(f'#{tc} {max_b - min_b}')

# 김민식님 풀이
# for tc in range(T):
#     N, M = map(int, input().split())
#     a = list(map(int, input().split()))
#
#     # 구간합의 변화량을 기록할 리스트 change를 생성한다. 최초값도 포함시키기 위해 0이 필요하다.
#     change = [0]
#     for i in range(N - M):
#         change.append(change[i] - a[i] + a[i + M])
#
#     # change 리스트에서 최댓값과 최솟값 탐색
#     max = change[0]
#     min = change[0]
#     for m in range(len(change)):
#         if change[m] > max:
#             max = change[m]
#         elif change[m] < min:
#             min = change[m]
#
#     answer = max - min
#     print(f'#{tc + 1} {answer}')
