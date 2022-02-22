class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1

    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.size

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
    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' + result
        return result





s1 = Stack(5)
s1.is_empty()
s1.push(1)
s1.is_empty()
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.pop()