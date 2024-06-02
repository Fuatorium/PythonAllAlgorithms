# Python Algorithms

This repository contains Python implementations of various algorithms, organized into different categories. Each algorithm is implemented in a separate Python file and stored in a relevant folder.

## Folder Structure

The repository is organized into the following folders:
- `Classic Encryption Algorithms`
- `Sorting Algorithms`
- `Search Algorithms`
- `Graph Algorithms`
- `Dynamic Programming`
- `Tree Algorithms`
- `Stack and Queue Algorithms`
- `Other Algorithms`

## Algorithms

### Sorting Algorithms

1. **Bubble Sort (bubble_sort.py)**
   - A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

2. **Selection Sort (selection_sort.py)**
   - An in-place comparison-based sorting algorithm that divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly selects the smallest element from the unsorted sublist and moves it to the sorted sublist.

3. **Insertion Sort (insertion_sort.py)**
   - A simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

4. **Merge Sort (merge_sort.py)**
   - A divide-and-conquer algorithm that splits the list into halves, recursively sorts each half, and merges the sorted halves to produce the sorted list.

5. **Quick Sort (quick_sort.py)**
   - A highly efficient sorting algorithm that uses a divide-and-conquer strategy to partition the array into sub-arrays and sort them independently.

6. **Heap Sort (heap_sort.py)**
   - A comparison-based sorting algorithm that builds a binary heap from the input data and then extracts the maximum or minimum element from the heap repeatedly to build the sorted array.

7. **Counting Sort (counting_sort.py)**
   - A non-comparison-based sorting algorithm that counts the number of occurrences of each unique element and uses this information to place each element in the correct position in the sorted array.

8. **Radix Sort (radix_sort.py)**
   - A non-comparison-based sorting algorithm that sorts integers by processing individual digits. It uses counting sort as a subroutine to sort elements based on their digits.

9. **Bucket Sort (bucket_sort.py)**
   - A distribution-based sorting algorithm that divides the input into several buckets, sorts each bucket individually using a different sorting algorithm, and then combines the sorted buckets to get the final sorted array.

10. **Shell Sort (shell_sort.py)**
    - An in-place comparison-based sorting algorithm that generalizes insertion sort to allow the exchange of items that are far apart. It uses a gap sequence to determine the interval between compared elements.

11. **Tim Sort (tim_sort.py)**
    - A hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data and is used as the standard sorting algorithm in Python and Java.

12. **Comb Sort (comb_sort.py)**
    - A comparison-based sorting algorithm that improves on bubble sort by using a gap sequence to compare and swap elements that are farther apart.

### Search Algorithms

1. **Linear Search (linear_search.py)**
   - A simple search algorithm that checks each element of the list sequentially until the desired element is found or the list is exhausted.

2. **Binary Search (binary_search.py)**
   - A search algorithm that finds the position of a target value within a sorted array by repeatedly dividing the search interval in half.

3. **Depth First Search (DFS) (dfs.py)**
   - A graph traversal algorithm that explores as far as possible along each branch before backtracking.

4. **Breadth First Search (BFS) (bfs.py)**
   - A graph traversal algorithm that explores all the neighbor nodes at the present depth before moving on to nodes at the next depth level.

5. **Jump Search (jump_search.py)**
   - A search algorithm for ordered lists that uses a fixed step size to jump ahead and then performs a linear search within the block where the target value may reside.

6. **Interpolation Search (interpolation_search.py)**
   - A search algorithm that improves on binary search for uniformly distributed data by estimating the position of the target value.

7. **Exponential Search (exponential_search.py)**
   - A search algorithm for unbounded or infinite lists that combines binary search with exponential step sizes.

8. **Fibonacci Search (fibonacci_search.py)**
   - A search algorithm that uses Fibonacci numbers to divide the array into smaller parts, reducing the search space logarithmically.

9. **Ternary Search (ternary_search.py)**
   - A search algorithm that divides the search interval into three parts and recursively checks which part contains the target value.

### Graph Algorithms

1. **Dijkstra's Algorithm (dijkstra.py)**
   - An algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks.

2. **A* Search Algorithm (a_star.py)**
   - A graph traversal and path search algorithm that is widely used in pathfinding and graph traversal. It uses heuristics to improve performance.

3. **Bellman-Ford Algorithm (bellman_ford.py)**
   - An algorithm for finding the shortest paths from a single source vertex to all other vertices in a weighted graph, which may have negative weight edges.

4. **Floyd-Warshall Algorithm (floyd_warshall.py)**
   - An algorithm for finding shortest paths in a weighted graph with positive or negative edge weights.

5. **Kruskal's Algorithm (kruskal.py)**
   - An algorithm for finding the minimum spanning tree of a graph, which finds a subset of the edges that forms a tree including every vertex, where the total weight of all the edges in the tree is minimized.

6. **Prim's Algorithm (prim.py)**
   - An algorithm that finds a minimum spanning tree for a connected weighted graph.

7. **Topological Sort (topological_sort.py)**
   - An algorithm for ordering the vertices in a directed acyclic graph (DAG) such that for every directed edge u v, vertex u comes before v in the ordering.

8. **Kosaraju's Algorithm (kosaraju.py)**
   - An algorithm to find the strongly connected components of a directed graph.

9. **Tarjan's Algorithm (tarjan.py)**
   - An algorithm to find the strongly connected components in a directed graph.

10. **Edmonds-Karp Algorithm (edmonds_karp.py)**
    - An implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network.

11. **Ford-Fulkerson Algorithm (ford_fulkerson.py)**
    - A method for computing the maximum flow in a flow network.

12. **Johnson's Algorithm (johnson.py)**
    - An algorithm for finding shortest paths between all pairs of vertices in a sparse, weighted, directed graph.

### Dynamic Programming

1. **Fibonacci Sequence (fibonacci_sequence.py)**
   - An algorithm to find the nth Fibonacci number using dynamic programming.

2. **Longest Common Subsequence (LCS) (longest_common_subsequence.py)**
   - An algorithm to find the longest subsequence common to two sequences.

3. **Longest Increasing Subsequence (LIS) (longest_increasing_subsequence.py)**
   - An algorithm to find the length of the longest increasing subsequence in a given sequence.

4. **0/1 Knapsack Problem (knapsack.py)**
   - An algorithm to solve the knapsack problem using dynamic programming.

5. **Matrix Chain Multiplication (matrix_chain_multiplication.py)**
   - An algorithm to find the most efficient way to multiply a given sequence of matrices.

6. **Edit Distance (edit_distance.py)**
   - An algorithm to find the minimum number of operations required to convert one string into another.

7. **Subset Sum Problem (subset_sum.py)**
   - An algorithm to determine if there is a subset of a given set with a sum equal to a given value.

8. **Coin Change Problem (coin_change.py)**
   - An algorithm to find the minimum number of coins required to make a given amount of change.

9. **Rod Cutting Problem (rod_cutting.py)**
   - An algorithm to find the maximum revenue obtainable by cutting up a rod and selling the pieces.

10. **Palindrome Partitioning (palindrome_partitioning.py)**
    - An algorithm to partition a string such that every substring is a palindrome.

11. **Maximum Subarray Problem (maximum_subarray.py)**
    - An algorithm to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum.

12. **Egg Dropping Problem (egg_dropping.py)**
    - An algorithm to find the minimum number of attempts needed to find the critical floor in the worst case.

### Tree Algorithms

1. **Binary Search Tree (BST) (binary_search_tree.py)**
   - An implementation of a binary search tree, which supports operations like insertion, deletion, and search.

2. **AVL Tree (avl_tree.py)**
   - A self-balancing binary search tree where the difference between the heights of left and right subtrees cannot be more than one for all nodes.

3. **Red-Black Tree (red_black_tree.py)**
   - A balanced binary search tree with an additional bit for keeping track of the color of each node, which helps ensure the tree remains balanced during insertions and deletions.

4. **Segment Tree (segment_tree.py)**
   - A tree data structure for storing intervals or segments, allowing for efficient range queries and updates.

5. **Fenwick Tree / Binary Indexed Tree (BIT) (fenwick_tree.py)**
   - A tree data structure that provides efficient methods for prefix sums and updates.

6. **Splay Tree (splay_tree.py)**
   - A self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again.

7. **B-tree (b_tree.py)**
   - A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.

8. **Trie (Prefix Tree) (trie.py)**
   - A tree-like data structure used to store a dynamic set of strings, where keys are usually strings.

9. **K-D Tree (k_d_tree.py)**
   - A space-partitioning data structure for organizing points in a k-dimensional space.

10. **R-Tree (r_tree.py)**
    - A tree data structure used for indexing multi-dimensional information such as geographical coordinates, rectangles, and polygons.

11. **Quad Tree (quad_tree.py)**
    - A tree data structure in which each internal node has exactly four children. It is used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

12. **Interval Tree (interval_tree.py)**
    - A tree data structure to hold intervals and allow efficiently querying which intervals overlap with a given interval or point.

13. **Cartesian Tree (cartesian_tree.py)**
    - A binary tree derived from a sequence of numbers, which serves as a priority queue with respect to the values.

### Stack and Queue Algorithms

1. **Stack Operations (stack_operations.py)**
   - Implementation of a stack with basic operations like push, pop, peek, and checking if the stack is empty.

2. **Queue Operations (queue_operations.py)**
   - Implementation of a queue with basic operations like enqueue, dequeue, front, and checking if the queue is empty.

3. **Priority Queue (priority_queue.py)**
   - Implementation of a priority queue using a binary heap.

4. **Circular Queue (circular_queue.py)**
   - Implementation of a circular queue with operations like enqueue, dequeue, and checking if the queue is full or empty.

5. **Deque (deque.py)**
   - Implementation of a double-ended queue (deque) with operations to add and remove elements from both ends.

6. **Monotonic Queue (monotonic_queue.py)**
   - Implementation of a monotonic queue that supports operations to maintain a queue where the elements are either in non-increasing or non-decreasing order.

### Other Algorithms

1. **Backtracking (backtracking.py)**
   - Implementation of the N-Queens problem using backtracking.

2. **Divide and Conquer (divide_and_conquer.py)**
   - Implementation of merge sort using the divide and conquer strategy.

3. **Greedy Algorithms (greedy_algorithms.py)**
   - Implementation of the activity selection problem using a greedy algorithm.

4. **Brute Force Algorithms (brute_force.py)**
   - Implementation of brute force string matching.

5. **Branch and Bound (branch_and_bound.py)**
   - Implementation of the 0/1 knapsack problem using the branch and bound method.

6. **Dynamic Connectivity (dynamic_connectivity.py)**
   - Implementation of the Union-Find data structure with path compression and union by rank.

7. **String Matching Algorithms**
   - **Knuth-Morris-Pratt (KMP) Algorithm (kmp_algorithm.py)**
     - Implementation of the KMP algorithm for string matching.
   - **Rabin-Karp Algorithm (rabin_karp.py)**
     - Implementation of the Rabin-Karp algorithm for string matching.
   - **Boyer-Moore Algorithm (boyer_moore.py)**
     - Implementation of the Boyer-Moore algorithm for string matching.

8. **Computational Geometry Algorithms**
   - **Convex Hull Algorithms (convex_hull.py)**
     - Implementation of Graham's scan for finding the convex hull.
   - **Line Intersection (line_intersection.py)**
     - Implementation of line segment intersection.
   - **Voronoi Diagram (voronoi_diagram.py)**
     - Implementation of Voronoi diagram using SciPy.

9. **Number Theory Algorithms**
   - **Sieve of Eratosthenes (sieve_of_eratosthenes.py)**
     - Implementation of the sieve of Eratosthenes for finding all prime numbers up to a specified integer.
   - **Euclidean Algorithm (euclidean_algorithm.py)**
     - Implementation of the Euclidean algorithm for finding the greatest common divisor (GCD) of two numbers.
   - **Modular Exponentiation (modular_exponentiation.py)**
     - Implementation of modular exponentiation.
   - **Chinese Remainder Theorem (chinese_remainder_theorem.py)**
     - Implementation of the Chinese Remainder Theorem.

10. **Randomized Algorithms**
    - **Quickselect (quickselect.py)**
      - Implementation of the quickselect algorithm for finding the kth smallest element in an unordered list.
    - **Reservoir Sampling (reservoir_sampling.py)**
      - Implementation of reservoir sampling.
    - **Monte Carlo Algorithms (monte_carlo.py)**
      - Implementation of the Monte Carlo algorithm for estimating the value of Pi.
    - **Las Vegas Algorithms (las_vegas.py)**
      - Implementation of a Las Vegas algorithm for quickselect.

11. **Compression Algorithms**
    - **Huffman Coding (huffman_coding.py)**
      - Implementation of Huffman coding for data compression.
    - **LZW (Lempel-Ziv-Welch) (lzw.py)**
      - Implementation of the LZW algorithm for data compression.
    - **Run-Length Encoding (RLE) (run_length_encoding.py)**
      - Implementation of run-length encoding.

12. **Cryptographic Algorithms**
    - **RSA Algorithm (rsa_algorithm.py)**
      - Implementation of the RSA encryption and decryption algorithm.
    - **Diffie-Hellman Key Exchange (diffie_hellman.py)**
      - Implementation of the Diffie-Hellman key exchange algorithm.
    - **Elliptic Curve Cryptography (ECC) (ecc.py)**
      - Implementation of basic operations in elliptic curve cryptography.
    - **Advanced Encryption Standard (AES) (aes.py)**
      - Implementation of AES encryption and decryption using the PyCryptodome library.
    - **Secure Hash Algorithms (SHA) (sha.py)**
      - Implementation of SHA-256 hashing using the hashlib library.
     
### Classical Encryption Algorithms

1. **Caesar Cipher (caesar_cipher.py)**
   - A substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

2. **Atbash Cipher (atbash_cipher.py)**
   - A substitution cipher where the letters of the alphabet are reversed. 'A' becomes 'Z', 'B' becomes 'Y', etc.

3. **Vigenère Cipher (vigenere_cipher.py)**
   - A polyalphabetic substitution cipher that uses a keyword to determine the shift for each letter.

4. **Playfair Cipher (playfair_cipher.py)**
   - A digraph substitution cipher that encrypts pairs of letters using a 5x5 matrix.

5. **Affine Cipher (affine_cipher.py)**
   - A substitution cipher where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.

6. **Rail Fence Cipher (rail_fence_cipher.py)**
   - A transposition cipher where the plaintext is written in a zigzag pattern on a number of 'rails' and then read line by line.

7. **Columnar Transposition Cipher (columnar_transposition_cipher.py)**
   - A transposition cipher that involves writing the plaintext out in rows and then reading the ciphertext off in columns one by one.

8. **Baconian Cipher (baconian_cipher.py)**
   - A substitution cipher in which each letter is replaced by a sequence of five characters consisting of 'A' or 'B'.

9. **Scytale Cipher (scytale_cipher.py)**
   - An ancient transposition cipher where a strip of parchment is wound around a cylinder and the message is written along the length of the cylinder.

10. **Keyword Cipher (keyword_cipher.py)**
    - A monoalphabetic substitution cipher where a keyword determines the substitution of letters.

11. **Beaufort Cipher (beaufort_cipher.py)**
    - A polyalphabetic substitution cipher similar to the Vigenère cipher but with a slightly different method for encryption.

12. **Gronsfeld Cipher (gronsfeld_cipher.py)**
    - A polyalphabetic substitution cipher very similar to the Vigenère cipher but uses digits (0-9) instead of letters in the key.

13. **Four-Square Cipher (four_square_cipher.py)**
    - Uses four 5x5 matrices arranged in a square to encrypt digraphs (pairs of letters).

14. **ADFGVX Cipher (adfgvx_cipher.py)**
    - Uses a combination of a Polybius square and a columnar transposition. It was used by the German Army during World War I.

15. **Bifid Cipher (bifid_cipher.py)**
    - Combines the Polybius square with transposition to achieve diffusion. It is a combination of substitution and transposition.

16. **ROT13 Cipher (rot13_cipher.py)**
    - A special case of the Caesar cipher where the shift is 13. It is commonly used in forums and online to obscure text.

17. **Morse Code (morse_code.py)**
    - A method used in telecommunication to encode text characters as sequences of dots and dashes.

18. **Pigpen Cipher (pigpen_cipher.py)**
    - A simple substitution cipher that exchanges letters for symbols based on a grid pattern.

## How to Run

To run any of the algorithms, simply navigate to the relevant folder and execute the Python file. For example, to run the Bubble Sort algorithm:

```sh
python Sorting\ Algorithms/bubble_sort.py
