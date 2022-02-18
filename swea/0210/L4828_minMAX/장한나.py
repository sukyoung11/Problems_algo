import sys
sys.stdin = open("input.txt")

T = int(input())


def max_min():
    N = int(input())
    numbers = list(map(int, input().split()))
    maxNum = numbers[0]
    minNum = numbers[0]

    for nth in range(1, N):
        if numbers[nth] >= maxNum:
            maxNum = numbers[nth]

        if numbers[nth] <= minNum:
            minNum = numbers[nth]

    result = maxNum - minNum
    return result

for tc in range(1, T+1):
    answer = max_min()
    print(f"#{tc} {answer}")
