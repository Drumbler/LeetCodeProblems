from collections import deque


class MyStack(object):
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        v = len(self.q) - 1
        for i in range(v):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return self.q == []


s = MyStack()
print(s.push(1))
print(s.push(2))
print(s.top())
print(s.pop())
print(s.empty())
