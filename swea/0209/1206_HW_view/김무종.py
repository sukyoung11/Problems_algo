import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    start = 2
    while start < len(buildings) - 2:
        max_building = 0

        for j in [(start - 2), (start - 1), (start + 1), (start + 2)]:
            if buildings[j] > max_building:
                max_building = buildings[j]

        green = buildings[start] - max_building

        if green > 0:
            answer += green
            start += 2
        else:
            start += 1
    print(f'#{i + 1} {answer}')


