import sys
sys.stdin = open('input.txt')
T = int(input())

for t in range(T):
    s =  list(input())
    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()

    print(f'#{t+1} {len(stack)}')






"""
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1

    def push(self,item):
        if self.is_full():
            print('stack overflow')
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            print('empty stack')
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -=1
        return item

    def peak(self):
        if self.is_empty():
            print('empty')
        else:
            return self.items[self.top]

    T = int(input())
    stack = []
    for t in range(T):
        s =  list(input())
        stack = Stack(len(s))

        for i in range(len(s)):
            if self.top == -1:
                stack.push(i)
            else:
                if self.peak == i:
                    stack.pop()
                else:
                    stack.push(i)
        print(stack.top)

 """

