import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def huffman_code_tree(node, bin_string=''):
    if node is None:
        return
    if node.left is None and node.right is None:
        huffman_code[node.symbol] = bin_string
    huffman_code_tree(node.left, bin_string + '0')
    huffman_code_tree(node.right, bin_string + '1')

def calculate_huffman_code(data):
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1
    heap = [Node(freq[char], char) for char in freq]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(heap, merged)
    huffman_code_tree(heap[0])
    return huffman_code

if __name__ == "__main__":
    data = "BCAADDDCCACACAC"
    huffman_code = {}
    huffman_code = calculate_huffman_code(data)
    print(f"Huffman Codes: {huffman_code}")
    encoded_data = ''.join(huffman_code[char] for char in data)
    print(f"Encoded Data: {encoded_data}")
