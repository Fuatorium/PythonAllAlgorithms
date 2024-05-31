import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def is_empty(self):
        return len(self.pq) == 0

    def insert(self, item):
        heapq.heappush(self.pq, item)

    def extract_min(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.pq)

    def peek(self):
        if self.is_empty():
            return None
        return self.pq[0]

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(10)
    pq.insert(20)
    pq.insert(5)
    print(f"Minimum item is {pq.peek()}")
    print(f"Extracted min item is {pq.extract_min()}")
    print(f"Minimum item after extraction is {pq.peek()}")
