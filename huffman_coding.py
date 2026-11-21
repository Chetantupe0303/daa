import heapq
from itertools import count


def build_codes(frequencies):
    serial = count()
    heap = [(frequency, next(serial), character, None, None)
            for character, frequency in frequencies.items()]
    heapq.heapify(heap)

    if not heap:
        return {}
    while len(heap) > 1:
        f1, _, c1, l1, r1 = heapq.heappop(heap)
        f2, _, c2, l2, r2 = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, next(serial), None,
                              (c1, l1, r1), (c2, l2, r2)))

    codes = {}

    def traverse(node, code):
        character, left, right = node
        if character is not None:
            codes[character] = code or "0"
            return
        traverse(left, code + "0")
        traverse(right, code + "1")

    _, _, character, left, right = heap[0]
    traverse((character, left, right), "")
    return codes


n = int(input("Enter number of characters: "))
frequencies = {}
for _ in range(n):
    character, frequency = input("Enter character and frequency: ").split()
    frequencies[character] = int(frequency)

print("Huffman codes:")
for character, code in build_codes(frequencies).items():
    print(f"{character} : {code}")
print("Time Complexity: O(n log n)")