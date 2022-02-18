import sys
sys.stdin = open('input.txt')

tc = int(input())

for count in range(tc):
    N = int(input())
    AandBs = []
    for _ in range(N):
        AandBs.append(list(map(int, input().split())))
    P = int(input())

    stops = []
    for _ in range(P):
        stops.append(int(input()))

    answers = [0 for _ in range(P)]

    for idx in range(len(stops)):
        for AandB in AandBs:
            if stops[idx] >= AandB[0] and stops[idx] <= AandB[1]:
                answers[idx] += 1


    print(f'#{count + 1}', end='')

    for answer in answers:
        print(f' {answer}', end='')

    print('')