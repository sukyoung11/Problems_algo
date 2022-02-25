import sys
sys.stdin = open('input.txt')

def cal(x,y,i):
    if i == '+':
        return x + y
    elif i == '-':
        return x - y
    elif i == '*':
        return x * y
    else:
        return x // y

T = int(input())
for t in range(T):
    array = input().split()
    num_list = []

    for item in array:
        if item in ['+','-','*','/']:
            if len(num_list) >= 2:
                y = num_list.pop()
                x = num_list.pop()
                num_list.append(cal(int(x),int(y),item))
            else:
                print(f'#{t+1} error')
                break
        elif item == '.':
            if len(num_list)==1:
                print(f'#{t+1} {num_list[0]}')
            else:
                print(f'#{t+1} error')
        else:
            num_list.append(item)

