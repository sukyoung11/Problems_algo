# combinations 으로 부분집합 만들기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    numbers = list(map(int,input().split()))
    N = len(numbers)

    for i in range(2 ** N): # i = 모든 경우의 개수, 선택 그 자체
        subset = []
        for scanner in range(N):
            if i & (1<< scanner):
                print(numbers[scanner],end=" ")
        print("")






