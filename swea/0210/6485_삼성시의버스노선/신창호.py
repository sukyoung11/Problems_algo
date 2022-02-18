import sys
sys.stdin = open('input.txt')


# TC 테스트케이스
# N 버스노선수
# A1 B1 1번 노선
# A2 B2 N번 노선
# P 정류장 수
# C1
# C2
# ...
# CP p번째 정류장


tc = int(input())
for t in range(1, tc+1):
    line_start = [0] * 501
    line_end = [0] * 501
    N = int(input())

    for i in range(1, N+1):
        line_start[i], line_end[i] = map(int, input().split())

    # 해당 정류장을 지나는 노선의 개수는?
    cnt = [0] * 5001
    for j in range(1, N+1):
        for k in range(line_start[j], line_end[j]+1):
            cnt[k] += 1

    # 정답 출력 부분
    # P = int(input())
    # print(f'#{t}', end=" ")
    # for k in range(1, P):
    #     tmp = int(input())
    #     print(answer[tmp], end=" ")
    # tmp = int(input())
    # print(answer[tmp])

    P = int(input())
    answer = []
    for _ in range(P):
        answer.append(cnt[int(input())])
    print(f'#{t}', " ".join(list(map(str, answer))))
