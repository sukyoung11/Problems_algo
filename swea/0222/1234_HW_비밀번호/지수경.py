import sys
sys.stdin = open('input.txt')

for t in range(10):
    N,s = input().split()
    password = list(s)

    stack = []
    for i in password:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    print(f'#{t+1} {"".join(stack)}')
