import sys
sys.stdin = open('input.txt')

# TC
# N Q
# L R
# L R

tc = int(input())  # test case 받아오기
for t in range(1, tc+1):
    N, Q = map(int, input().split())  # N, Q 받아오기
    boxes = [0] * N  # boxes 생성
    for i in range(1, Q+1):  # 상자 교체작업
        L, R = map(int, input().split())  # L, R 받아오기
        for j in range(L-1, R):
            boxes[j] = i

    # row <- list to string
    boxes = " ".join(list(map(str, boxes)))
    print(f'#{t} {boxes}')
