import sys
sys.stdin = open('input.txt')

result = []
for tc in range(1, 11):
    dump = int(input())
    numbers = list(map(int, input().split()))

    for i in range(dump):
        max_val = min_val = numbers[0]
        max_idx = min_idx = 0

        for j in range(100):
            if max_val < numbers[j]:
                max_val = numbers[j]
                max_idx = j
            elif min_val > numbers[j]:
                min_val = numbers[j]
                min_idx = j

        numbers[max_idx] -= 1
        numbers[min_idx] += 1

        max_val = min_val = numbers[0]
        for k in range(100):
            if max_val < numbers[k]:
                max_val = numbers[k]
            if min_val > numbers[k]:
                min_val = numbers[k]

    print(f'#{tc} {max_val - min_val}')