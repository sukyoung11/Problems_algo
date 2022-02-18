import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())
print(T)

# 테스트 케이스 별로 카트 구성
for _ in range(T):
    card = list(map(int, input()))

    # 카드 전체 범위에서 0번째 카드를 기준으로 시작해서 인접한 카드 값의 대소 비교 후, 크면 오른쪽으로 이동
    for i in range(len(card), 0, -1):  # card의 전체범위부터 ~ 역순으로 최소범위(0)까지
        for j in range(i-1):           # 기준 값과 다음 인접 값의 대소 비교를 하므로 마지막 항목을 빼서 인덱싱 오류를 피함
            if card[j] > card[j+1]:    # 기준 값이 다음 값보다 크면
                card[j], card[j+1] = card[j+1], card[j]  # 기준 값과 다음 값의 자리를 바꾼다.

    # 0~9 까지의 개수를 세기 위해 빈 리스트 생성. 다만, run 계산을 위해 두 칸 더 만듬
    arr = [0] * 12
    run = 0
    tri = 0
    # 제시된 카드 전체를 순회하며 각 카드에 해당하는 값을 arr 인덱싱에 그대로 += 1로 카운트
    for k in range(len(card)):
        arr[card[k]] += 1
        # 각 카드 값이 해당하는 수를 인덱싱 번호에 맞게 카운트 한 arr의 전체 범위를 순회
        for g in range(len(arr)):
            # 연속된 숫자 3개로 조합된 카드 구성이라면 run += 1 하고, 각 해당하는 값들은 -= 1
            if arr[g] > 0 and arr[g+1] > 0 and arr[g+2] > 0:
                run += 1
                arr[g] -= 1
                arr[g+1] -= 1
                arr[g+2] -= 1
            # 같은 숫자가 3장 있는 카드 구성이라면, tri += 1 하고, 해당하는 값은 -= 3
            if arr[g] >= 3:
                tri += 1
                arr[g] -= 3
    # run 과 tri의 합은 최대 2 이고, 만약 2라면 'baby-gin' 출력
    if run + tri >= 2:
        print('baby-gin')
    # 합이 2 미만이라면, 'no baby-gin' 출력
    else:
        print('no baby-gin')
