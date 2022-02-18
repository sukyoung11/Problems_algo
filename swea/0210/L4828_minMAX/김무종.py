import sys
sys.stdin = open('input.txt')

def max_min(list_a):
    max_number = min_number = list_a[0]
    for j in range(1, len(list_a)):
        if list_a[j] > max_number:
            max_number = list_a[j]
        if list_a[j] < min_number:
            min_number = list_a[j]
    return max_number - min_number

T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{i} {max_min(numbers)}')
