import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    new_result = []
    for i in range(N-M+1):
        count = 0
        result = 0
        while count < M:
            result += numbers[i]
            count += 1
            i += 1
        new_result.append(result)

    print(f'#{tc} {max(new_result) - min(new_result)}')
