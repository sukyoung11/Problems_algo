import sys
sys.stdin = open('input.txt')







'''교수님
T = 10
for tc in range(1, T+1):
    width = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    
    for idx in range(2, width-2):
        highest_buildings = max(buildings[idx-2], buildings[idx-1], buildings[idx+1], buildings[idx+2])
        
        if buildings[idx] > highest_building:
            cnt += buildings[idx] - highest_building
        
        print(f'#{tc} {cnt})
'''