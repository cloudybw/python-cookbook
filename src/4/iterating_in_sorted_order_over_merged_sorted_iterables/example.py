# Iterating over merged sorted iterables

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
c = [2, 6, 5, 11]
#for c in heapq.merge(a, b):
#    print(c)

# c is NOT sorted, still runnable, but result is incorrect
for d in heapq.merge(a, c):
    print(d)
