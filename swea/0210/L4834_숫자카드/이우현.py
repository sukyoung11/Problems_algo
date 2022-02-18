import sys
sys.stdin = open('input.txt')

# 15분

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    list_n = [0] * 10
    # print(numbers)
    for j in range(len(list_n)):
        for n in numbers:
            if j == n:
                list_n[j] += 1

    my_max = 0
    for j in range(len(list_n)):
        if my_max <= list_n[j]:
            my_max = list_n[j]
    # print(list_n)
    # print(my_max)
    result = []
    for j in range(len(list_n)):
        if my_max == list_n[j]:
            k = [j, list_n[j]]
            result.append(k)
    ans = ' '.join(list(map(str, result[-1])))
    print(f'#{tc} {ans}')