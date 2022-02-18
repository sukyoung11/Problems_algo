import sys
sys.stdin = open('input.txt')


def my_sum(M, N, numbers):
    sum_list = []

    # 구간합 리스트 만들기
    for i in range(N - M + 1):
        M_sum = 0

        for j in range(M):
            M_sum += numbers[i + j] # 인덱스 i부터 N개의 숫자를 sum

        sum_list.append(M_sum)  # 합친 애들 리스트에 추가

    return sum_list


T = int(input())

for tc in range(T):
    # 입력
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = my_sum(M, N, numbers) # 구간합 리스트

    # min, max 초기값 설정
    my_min = sum_list[0]
    my_max = sum_list[0]

    # min, max 수행
    for num in sum_list[1:]:
        if num > my_max:
            my_max = num
        if num < my_min:
            my_min = num

    answer = my_max - my_min # 구간합의 최대 최소 차

    print(f'#{tc + 1} {answer}')