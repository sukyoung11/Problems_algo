import sys
sys.stdin = open("input.txt")

num_of_test = int(input())

for test in range(1, num_of_test+1):
    number = int(input())

    decimal = [2, 3, 5, 7, 11]
    sup = [0] * 5

    print(f'#{test}', end = '')

    for i in range(5):
        while 1:
            if number % decimal[i] == 0:
                sup[i] += 1
                number //= decimal[i]
            else:
                print(f' {sup[i]}', end='')
                break
    print()