import sys
sys.stdin = open('input.txt')

# TC
# N
# ai*N
# ...

tc = int(input())
for t in range(1, tc+1):
    N = input()
    numbers = list(map(int, list(input())))

    counts = [0]*10
    for number in numbers:
        counts[number] += 1

    max_num = 0
    max_count = 0
    for i in range(len(counts)):
        if counts[i] >= max_count:
            max_num = i
            max_count = counts[i]
    print(f'#{t}', max_num, max_count)
