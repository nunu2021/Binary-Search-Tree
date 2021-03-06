
 ## Heaps
 ![alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/MinHeapAndMaxHeap.png)
 
 **Heaps** concrete data structures. What are concrete data structures? Well, there are two types of data structures: Abstract Data Structures(ADT) and Concrete Data Structures(CDT). An ADT determines the interface, while the CDT define the implementation.
 Here are  a couple of pros for each type of data structure:
 
 #### CDT:
  - specify performence garuntees
  - are implemented
  - can be meddled with to optimize code
  
 #### ADT
 - secure
 - high level
 - interfaces(like arrays)
 - have several overarching data, and operations rather than specific
 
 In a heap tree, the value in a node is always smaller than both of its children. This is called the heap property. This is different from a binary search tree, in which only the left node will be smaller than the value of its parent.
 
 ### Why Heap?
 The heap implementation of the priority queue guarantees that both pushing (adding) and popping (removing) elements are logarithmic time operations. This means that the time it takes to do push and pop is proportional to the base-2 logarithm of the number of elements.

Logarithms grow slowly. The base-2 logarithm of fifteen is about four, while the base-2 logarithm of a trillion is about forty. This means that if an algorithm is fast enough on fifteen elements, then it’s going to be only ten times slower on a trillion elements and will probably still be fast enough.
 
 A priority queue, and a heap as an implementation of a priority queue, is useful for programs that involve finding an element that is extreme in some way.
 
 ## Implementation of Heap
 
 I will be using the Python module **heapq**. The Python heapq module, and the heap data structure in general, is not designed to allow finding any element except the smallest one. For retrieval of any element by size, a better option is a **binary search tree**.
 
 Here are a couple of real world applications for Heap:
 - Getting the three most popular blog posts from hit data
- Finding the fastest way to get from one point to the other
- Predicting which bus will be the first to arrive at a station based on arrival frequency
 
 