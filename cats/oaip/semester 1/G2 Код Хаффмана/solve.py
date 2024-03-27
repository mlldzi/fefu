import heapq


def build_huffman_tree(freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:])


def huffman_encoding(freq):
    tree = build_huffman_tree(freq)
    huffman_codes = {}
    for symbol, code in tree:
        huffman_codes[symbol] = code
    return huffman_codes


with open("input.txt", "r", encoding="utf-8") as f, open("output.txt", "w", encoding="utf-8") as g:
    n = int(f.readline())
    nums = [int(f.readline().strip()) for x in range(n)]
    freq = {str(x): x for x in nums}
    huffman_codes = huffman_encoding(freq)
    for num in nums:
        g.write(huffman_codes[str(num)] + "\n")
