import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = int(input())
for t in range(T):
    test = input()
    numbers = input().split()
    order = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']


    result = []
    for i in order:
        for number in numbers:
            if number == i:
                result.append(number)

    print(f'#{t+1}\n{" ".join(result)}')

