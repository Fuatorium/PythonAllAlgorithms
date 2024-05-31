class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

class ITNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None

def insert(root, interval):
    if root is None:
        return ITNode(interval)
    l = root.interval.low
    if interval.low < l:
        root.left = insert(root.left, interval)
    else:
        root.right = insert(root.right, interval)
    if root.max < interval.high:
        root.max = interval.high
    return root

def do_overlap(i1, i2):
    if i1.low <= i2.high and i2.low <= i1.high:
        return True
    return False

def overlap_search(root, interval):
    if root is None:
        return None
    if do_overlap(root.interval, interval):
        return root.interval
    if root.left is not None and root.left.max >= interval.low:
        return overlap_search(root.left, interval)
    return overlap_search(root.right, interval)

if __name__ == "__main__":
    intervals = [Interval(15, 20), Interval(10, 30), Interval(17, 19), Interval(5, 20), Interval(12, 15), Interval(30, 40)]
    root = None
    for interval in intervals:
        root = insert(root, interval)
    query = Interval(6, 7)
    result = overlap_search(root, query)
    if result is not None:
        print(f"Overlaps with [{result.low}, {result.high}]")
    else:
        print("No overlap found")
