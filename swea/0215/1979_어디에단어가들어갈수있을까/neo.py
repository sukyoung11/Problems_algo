import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    matrix = [[0] * (N+2)]
    for _ in range(N):
        row = [0, *list(map(int, input().split())), 0]
        matrix.append(row)
    matrix.append([0] * (N+2))

    # 단어가 들어갈 수 있는 개수
    count = 0

    for i in range(1, N+2):
        # 빈칸의 길이
        size = 0

        for j in range(1, N+2):
            # 빈칸일 경우
            if matrix[i][j]:
                size += 1
            # 빈칸이 아닐 경우
            else:
                if size == K:
                    count += 1
                size = 0

        for j in range(1, N+2):
            # 빈칸일 경우
            if matrix[j][i]:
                size += 1
            # 빈칸이 아닐 경우
            else:
                if size == K:
                    count += 1
                size = 0

    print(f'#{tc} {count}')
