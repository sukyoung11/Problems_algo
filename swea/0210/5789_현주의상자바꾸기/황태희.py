import sys
sys.stdin = open('input.txt')

tc = int(input())

for count in range(tc):
    N, Q = map(int, input().split())
    boxes = [0 for _ in range(N)]
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for idx in range(L - 1, R):
            boxes[idx] = i

    print(f'#{count + 1}', end = '')

    for box in boxes:
        print(f' {box}', end = '')

    print('')
