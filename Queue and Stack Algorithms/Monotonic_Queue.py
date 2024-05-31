from collections import deque

class MonotonicQueue:
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def max(self):
        return self.deque[0]

    def pop(self, value):
        if self.deque and self.deque[0] == value:
            self.deque.popleft()

if __name__ == "__main__":
    mq = MonotonicQueue()
    mq.push(3)
    mq.push(1)
    mq.push(5)
    mq.push(2)
    print(f"Current max is {mq.max()}")
    mq.pop(5)
    print(f"Current max after pop is {mq.max()}")
