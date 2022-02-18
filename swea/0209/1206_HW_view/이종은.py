import sys
sys.stdin = open('input.txt')

# 테스트 케이스는 10 이라고 한다.
n = 10

# 마지막 출력 넘버링 때문에 범위 1 ~ n+1 지정
for i in range(1, n+1):
    row = int(input())
    col = list(map(int, input().split()))
    nice_home = 0
    # 기준 삼을 건물을 전체 범위에서 순회. 양끝 2칸은 집이 없으므로 범위에서 제외
    for h in range(2, len(col)-2):
        compare = []
        # 기준 건물 중심으로 양옆 2 건물, 총 4 건물이 전부 기준 건물보다 낮다면,
        if col[h] - col[h-2] > 0 and col[h] - col[h-1] > 0 and col[h] - col[h+1] > 0 and col[h] - col[h+2] > 0:
            # 4 건물 중에 가장 높은 건물을 도출하기 위해 4 건물 전부 빈 리스트에 저장
            compare.append(col[h-2])
            compare.append(col[h-1])
            compare.append(col[h+1])
            compare.append(col[h+2])

            # 4 건물 중 가장 높은 건물을 찾기 위한 식
            max_compare = compare[0]
            for j in range(1, len(compare)):
                if compare[j] > max_compare:
                    max_compare = compare[j]
            # 기준 건물과 4 건물 중 가장 높은 건물의 높이 차가 전망 좋은 세대의 개수
            nice_home += col[h] - max_compare

    print(f'#{i} {nice_home}')
