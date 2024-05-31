class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return len(self.deque) == 0

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.deque.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.deque.pop()

    def front(self):
        if self.is_empty():
            return None
        return self.deque[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.deque[-1]

if __name__ == "__main__":
    deque = Deque()
    deque.add_front(10)
    deque.add_rear(20)
    deque.add_front(5)
    print(f"Front item is {deque.front()}")
    print(f"Rear item is {deque.rear()}")
    print(f"Removed front item is {deque.remove_front()}")
    print(f"Removed rear item is {deque.remove_rear()}")
