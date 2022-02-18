import sys
sys.stdin = open('input.txt')


def my_min(numbers):
    my_min_result = numbers[0]

    for number in numbers[1:]:
        my_min_result = number if number < my_min_result else my_min_result
    return my_min_result


def my_max(numbers):
    my_max_result = numbers[0]

    for number in numbers[1:]:
        my_max_result = number if number > my_max_result else my_max_result
    return my_max_result


num_of_test = int(input())

for case in range(1, num_of_test+1):

    length_of_num = int(input())
    numbers = list(map(int, input().split()))
    result = my_max(numbers) - my_min(numbers)

    print(f'#{case} {result}')

