import sys
sys.stdin = open("input.txt")

def my_max(nums):
    result = nums[0]

    for num in nums[1:]:
        result = num if num >= result else result
    
    return result

def check_light(buildings, num_of_buildings):
    result = 0

    for i in range(2, num_of_buildings-2):
        result += my_max([0, buildings[i] - my_max([buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]])])

    return result


num_of_investigation = 10

for investigation in range(1, num_of_investigation+1):
    num_of_buildings = int(input())
    buildings = [int(char) for char in input().split()]
    
    result = check_light(buildings, num_of_buildings)

    print(f'#{investigation} {result}')


