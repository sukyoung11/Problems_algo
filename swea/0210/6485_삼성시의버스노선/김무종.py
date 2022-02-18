import sys
sys.stdin = open('input.txt')

def get_bus(n):
    list1 = [0] * n
    idx = 0
    for p in range(n):
        x = int(input())
        for A_B in A_B_list:
            if A_B[0] <= x and x <= A_B[1]:
                list1[p] += 1
    return ' '.join(map(str, list1))


T = int(input())
for i in range(1, T+1):
    N = int(input())
    idx = 0
    A_B_list = []
    while True:
        A_B_list.append(list(map(int, input().split())))
        idx = idx + 1
        if idx == N:
            break
    P = int(input())
    print(f'#{i}', get_bus(P))
