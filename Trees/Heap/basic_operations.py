import heapq # the heap module used on python

a = [3,5,1,2,6,8,7]
heapq.heapify(a) # returns array into a heap -> [1, 2, 3, 5, 6, 8, 7]
print(a)


#  POP - pops the smallest value while maintaining the heap property

a = [1, 2, 3, 5, 6, 8, 7]
print(heapq.heappop(a))
print(a)

# PUSH - pushing an element to the heap while preserving the heap property

a = [2, 5, 3, 7, 6, 8]
heapq.heappush(a, 4)

a = [2, 5, 3, 7, 6, 8, 4]
heapq.heappop(a)
heapq.heappop(a)
heapq.heappop(a)
print(a)

# The Python heapq module also defines two more operations:
#
# heapreplace() is equivalent to heappop() followed by heappush().
# heappushpop() is equivalent to heappush() followed by heappop().

a = [2, 5, 3, 7, 6, 8, 4]
