import heapq

def find_median(n, numbers):
    min_heap = []
    max_heap = []
    medians = []

    for i in range(n):
        num = numbers[i]
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        medians.append(-max_heap[0])

    return medians

with open('input.txt', 'r') as file:
    n = int(file.readline())
    numbers = list(map(int, file.readline().split()))

medians = find_median(n, numbers)

with open('output.txt', 'w') as file:
    for median in medians:
        file.write(str(median) + ' ')
        
