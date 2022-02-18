import sys
sys.stdin = open('input.txt')

for count in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = 0
    i = 2
    while i < len(buildings) - 2:
        max_building = 0

        for j in [(i - 2), (i - 1), (i + 1), (i + 2)]:
            if buildings[j] > max_building:
                max_building = buildings[j]

        green_zone = buildings[i] - max_building

        if green_zone > 0:
            answer += green_zone
            i += 2
        else:
            i += 1
    print(f'#{count + 1} {answer}')