import sys
sys.stdin = open("input.txt")

# 테스트케이스받기
T = int(input())

for tc in range(1, T+1):
    N = int(input()) #받을 카드개수
    numbers = list(map(int, input())) #저는 정수형 숫자가 있는 리스트로 카드숫자 받았습니다.
    # numbers = list(input())
    count_list = [0] * 10 # 0-9까지 숫자카드를 받을 수 있으므로
    for i in numbers:        # 카드숫자를 읽고 카운트리스트에 카운트하기
        count_list[i] += 1
    max = 0
    for i in range(10):         # 카드 개수 맥스값을 찾기 위해 카운트리스트에 저장된 값 읽기
        if count_list[i] >= max:
            max = count_list[i]
            max_num = i          # 가장 많은 카드개수의 카드숫자 저장
    print(f'#{tc} {max_num} {max}')
