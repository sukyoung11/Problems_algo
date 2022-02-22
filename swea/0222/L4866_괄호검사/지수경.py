import sys
sys.stdin = open('input.txt')
T = int(input())

for t in range(T):
    s= input()
    bracket = ['(',')','{','}']
    stack=[]

    for i in s:
        if i in bracket:
            if len(stack) ==0:  # stack이 비어있는 경우
                stack.append(i)
            else:              # stack이 비어있지 않은 경우
                if i =='}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(i)

                elif i == ')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        stack.append(i)

                else:
                    stack.append(i)


    if len(stack) == 0:
        print(f'#{t + 1} {1}')
    else:
        print(f'#{t + 1} {0}')
