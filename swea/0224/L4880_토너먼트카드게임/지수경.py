import sys
sys.stdin = open('input.txt')

def rsp(x,y):
    if x[1] ==1 and y[1] == 3:
        return x
    elif x[1] == 3 and y[1] == 1:
        return y
    else:
        if x[1]>=y[1]:
            return x
        else:
            return y

def game(array):
    if len(array) == 1:
        print(array[0])
        return array[0]
    elif len(array) == 2:
        print(rsp(array[0],array[1]))
        return rsp(array[0],array[1])
    else:
        print(array[0: ((len(array)+1)//2)])
        left = game(array[0: (len(array)+1)//2])
        print(array[((len(array)+1)// 2):])
        right = game(array[(len(array)+1) // 2:])
        print(rsp(left, right))
        return rsp(left, right)

T = int(input())
for t in range(T):
    N = int(input())
    input_array = list(map(int,input().split()))
    students = []
    for num,case in enumerate(input_array):
        students.append([num+1,case])
    print(students)
    print(f'#{t+1} {game(students)[0]}')