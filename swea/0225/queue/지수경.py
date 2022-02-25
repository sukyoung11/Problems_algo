class Queue:
    def __init__(self, *args):
        self.items = list(args)

        def peek(self):
            return self.items[0]

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError('queue is empty')
        else:
            item = self.peak()
            self.items.pop()
            return item

    def is_empty(self):
        return

