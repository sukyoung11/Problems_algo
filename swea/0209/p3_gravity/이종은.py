import sys
sys.stdin = open('input.txt')

# 테스트 케이스 횟수
T = int(input())
print(T)

# 각 케이스별로 상자 개수와 높이
for tc in range(T):
    box_total = int(input())
    boxes = list(map(int, input().split()))
    print(box_total)
    print(boxes)

    # 각 위치별로 쌓인 상자 높이보다 낮은 상자 높이를 가진 위치의 개수가 각 위치의 상자가 가질 수 있는 최대 낙차값
    # 각 위치별 최대 낙차 값을 저장하기 위해 빈 리스트 compare 생성
    compare = []
    # 상자 높이 비교를 위해, boxes[i]를 기준으로 삼음, 비교 대상이 아니라 기준이기 때문에 마지막 상자는 미포함
    for i in range(len(boxes)-1):
        max_gap = 0
        # 상자 높이 비교를 위해, boxes[j]를 비교 대상으로 삼음, 비교 대상이기 때문에 기준 다음 인덱싱 [i+1]부터 마지막 인덱싱까지
        for j in range(i+1, len(boxes)):
            # 순회하는 비교 대상보다 기준이 클 때마다 max_gap += 1
            if boxes[i] > boxes[j]:
                max_gap += 1
        # 각 기준별 max_gap을 compare 리스트에 삽입
        compare.append(max_gap)

    # compare에서 max 값 도출
    compare_gap = compare[0]
    for k in range(1, len(compare)-1):
        if compare[k] > compare_gap:
            compare_gap = compare[k]

    print(compare_gap)

