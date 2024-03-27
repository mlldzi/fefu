from collections import deque

n, k = map(int, input().split())
last = -k
visitors = list(map(int, input().split()))
deque = deque()
result = 0

for visitor in visitors:

    if deque:
        while deque and visitor >= k + last:
            last += k
            deque.popleft()

    if visitor >= k + last:
        last = visitor
    else:
        deque.append(visitor)
    result = max(len(deque), result)

print(result)
