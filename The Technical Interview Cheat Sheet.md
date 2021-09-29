## Helpful Links
- [technical interviews](https://www.cs.cmu.edu/~07131/f19/topics/extratations/interviews/interviews.pdf)

## Data Structure Basics
### Abstract Data Types v.s. implementations
- list: arraylist, linkedlist
- set: hashset, treeset
- map: hashmap, treemap
- stack: linkedlist, list
- queue: linkedlist, list
- priority queue: heap


### **Array**
#### Definition:
- Stores data elements based on an sequential, most commonly 0 based, index.
- Based on [tuples](http://en.wikipedia.org/wiki/Tuple) from set theory.
- They are one of the oldest, most commonly used data structures.

#### What you need to know:
- Optimal for indexing; bad at searching, inserting, and deleting (except at the end).
- **Linear arrays**, or one dimensional arrays, are the most basic.
  - Are static in size, meaning that they are declared with a fixed size.
- **Dynamic arrays** are like one dimensional arrays, but have reserved space for additional elements.
  - If a dynamic array is full, it copies its contents to a larger array.
- **Multi dimensional arrays** nested arrays that allow for multiple dimensions such as an array of arrays providing a 2 dimensional spacial representation via x, y coordinates.

#### Time Complexity:
- Indexing:         Linear array: O(1),      Dynamic array: O(1)
- Search:           Linear array: O(n),      Dynamic array: O(n)
- Optimized Search: Linear array: O(log n), Dynamic array: O(log n)
- Insertion:        Linear array: n/a        Dynamic array: O(n) 
- Popping: O(1) to pop the last element of a Python list, and O(N) to pop an arbitrary element (since the whole rest of the list has to be shifted)


### **Linked List**
#### Definition:
- Stores data with **nodes** that point to other nodes.
  - Nodes, at its most basic it has one datum and one reference (another node).
  - A linked list _chains_ nodes together by pointing one node's reference towards another node.
- header: contain size and first node of the LinkedList

#### What you need to know:
- Designed to optimize insertion and deletion, slow at indexing and searching.
- **Doubly linked list** has nodes that also reference the previous node.
- **Circularly linked list** is simple linked list whose **tail**, the last node, references the **head**, the first node.
- **Stack**, commonly implemented with linked lists but can be made from arrays too.
  - Stacks are **last in, first out** (LIFO) data structures.
  - Made with a linked list by having the head be the only place for insertion and removal.
- **Queues**, too can be implemented with a linked list or an array.
  - Queues are a **first in, first out** (FIFO) data structure.
  - Made with a doubly linked list that only removes from head and adds to tail.

#### Time Complexity:
- Indexing:         Linked Lists: O(n)
- Search:           Linked Lists: O(n)
- Optimized Search: Linked Lists: O(n)
- Insertion:        Linked Lists: O(1)

### ***Heap***
#### Definition:
- completeness: Every level (except last) completely filled. Nodes on bottom level are as far left as possible.
- heap order: maxHeap: every element <= its parent, but bigger element can be deeper in the tree

#### What you need to know:
- used to implement priority queue
- ``add(e)``
	- put the element at the leftmost empty node
	- bubble up while greater than its parent
- ``poll(e)``
	- save root in a local variable
	- assign last value to root, delete last node
	- bubble down: while less than a child, swap with the greater child
- children of node k: 2k+1, 2k+2

#### Time Complexity: 
- add: O(log n)
- poll: O(log n)
- peek: O(1)
- contains: O(n)
- remove: O(n)

### ***Graph***
- two vertices are adjacent if connected by one edge
- common graph representation: 
	- adjacency list: e.g. map from vertice to its neighbors; linkedlist, where each node contains vertex label and linkedlist of neighbors; array where each element is a linkedlist
	- adjacency matrix: arr[i][j] == 1 iff there is an edge from i to j
- space: 
	- adjacency list: O(|V| + |E|)
	- adjacency matrix: O(|V|^2)
- time to visit all edges:
	- adjacency list: O(|V| + |E|)
	- adjacency matrix: O(|V|^2)
- time to determine whether an edge from v1 to v2 exists:
	- adjacency list: O(|V| + outdegree of v1)
	- adjacency matrix: O(1)
- in a directed graph: 
	- outdegree of u: #edges where u is the source
	- indegree of u: #edges where u is the sink
- in an undirected graph: 
	- degree of u: #edges where u is an endpoint
- sparse: |E| << |V|^2, adjacency list better
- dense: |E| ~ |V|^2, adjacency matrix better
- topological order: and ordering of verticies as v1, v2, ..., vn, such that for every edge (vi, vj), it holds that i < j.
	- directed graph can be topologically ordered iff no cycle
	- acyclic: no cycle
- planar: can be drawn on the plane w/o any edge crossin
	- every planar graph is 4-colorable

### **Tree**
- an undirected graph if there is exactly one simple path between every vertex
- |E| = |V| - 1
- connected
- no cycles
- **spanning tree** of a connected graph (V, E) is a subgraph that is a tree
	- same set of vertices
	- maximal set of edges that contains no cycles / minimal set of edges that connect all vertices
	- ```
		find spannning tree (subtractive): 
			start with the whole graph
			while there is still a cycle:
				pick an edge from it and delete, graph remains connected
		```
	- but will throw out too many edges if graph dense
	- ```
		find spannning tree (additive): 
			while graph not connected:
				choose an edge that connects two components, and add it
				graph still has no cycle
		```

- check if a graph has cycle, similar to dfs:
	```
	def has_cycle(v):
		s = [v]
		visited = {v}
		while s:
			curr = s.pop()
			if curr in visited:
				return True
			for elem in v.neighbors:
				s.append(elem)
		return False
	```
- **minimum spanning tree (MST)**
	- suppose edge has weight > 0
	- sum of weights is minimum
- find MST
	- Kruskal's algorithm:
		```
		start with all nodes and no edges
		each step, add an edge that does not form a cycle with minimum weight 
		```
	- Prim's algorithm
		```
		start with one node
		each step, add an edge connected to the starting node with minimum weight
		the constructed tree always connected
		```
	- if edge weights all different, the Kruskal and Prim find the same MST


### **Hash Table or Hash Map**
#### Definition:
- Stores data with key value pairs.
- **Hash functions** accept a key and return an output unique only to that specific key / given a value **hashcode** to be put in the table, returns an index of where to put it
	- This is known as **hashing**, which is the concept that an input and an output have a one-to-one correspondence to map information.
  	- Hash functions return a unique address in memory for that data.
	- knows nothing about the table size, thus need to mod table_size
	- perfect hash function: map each input to a different index in the table
		- impossible
		- don't know size(table)
		- #possible values >> table size

#### What you need to know:
- Designed to optimize searching, insertion, and deletion.
- **Hash collisions** are when a hash function returns the same output for two distinct inputs.
	- multiple inputs are hashed to the same bucket
  	- All hash functions have this problem.
  	- This is often accommodated for by having the hash tables be very large.
	- solution: 
		- **chaining**: each bucket contains a linkedlist of items hashed to it
			- uses more memory
			- worst case: O(n), all elements hashed to one bucket
		- **open addressing**: each bucket contains one element, look in successive array element to find a place for new item
			- when removing an element, mark it as NP (not present), so when searching for an element, could keep looking
			- stop searching until it finds a null or the element you're searching for
			- clustering: nearby hashes have similar probe sequences, so more collision
			- linear probing: i, i+1, i+2, i+3, ..., 
				- problem: clustering
				- Deletion will be a problem. If one key involves a chain of several probes, it will be lost if somewhere along the chain, one of the other keys is removed, leaving an empty slot. Thus, you can't find the value stored after probing.
			- quadratic probing: i, i+1, i+4, i+9, ..., requires the len(table) to be a prime so have access to every bucket
- another problem: not all buckets get to used
- Hashes are important for associative arrays and database indexing.
- java.lang.Objects hashCode()
	- returns memory address of the object by default
	- if override equals, must override hashCode()
	- a.equals(b) returns true iff a and b are the same object
	- if equal, then should have the same hashcode and hashed to the same bucket
- **load factor** \lambda = # of entries / lenth of array
	- if \lambda = 1/2, expected # of probes = 2
	- if \lambda > 1/2, no longer expected constant operation
- expected time of add, contains, remove:
	- chaining
		- worst case: O(n), all elements hashed to the first buckect, and clustering at the front
		- if load factor small: O(1), most cases search length = 0, one case search length = n, 
		```
			((n-1)*0 + 1 * n) / len(table) = n/len(table) = load factor
		````
		- average chain length = load factor
	- linear probing
		- num of probes = 1/(1-\lambda)
- need to keep the size in a good range, not too many collision, not too large wasted memory
- **resizing**
	- when load factor too big, create a new array twice the size
	- move values into the new array
	- ArrayList does the same
	- dynanmic resizing: double the array, rehash all elements
	- amortize the cost of resizing over the time for adding elements
- HashMap in Java
	- computes key.hashCode(), so no duplicate key
	- default load factor = 0.75
	-  any class can serve as a key if and only if it overrides the equals() and hashCode() method
	- The bucket is a linkedlist but not java.util.Linkedlist. HashMap has its own implementation of the linkedlist. Therefore, it traverses through linkedlist and compares keys in each entry using keys.equals() until equals() returns true. Then, the value object is returned.
#### Time Complexity:
- Indexing: O(1) amortized
- Search: O(1), worst: O(n)
- Insertion: O(1), worst: O(n)


### **Binary Tree**
#### Definition:
- Is a tree like data structure where every node has at most two children.
  - There is one left and right child node.

#### What you need to know:
- depth: the length of the path to the root
- height: length of the longest path from the root to a leaf
- perfect tree: #node = 2^{h+1} - 1
- complete binary tree: Every level, except last, is completely filled, nodes on bottom level as far left as possible. No holes.
- Designed to optimize searching and sorting.
- A **degenerate tree** is an unbalanced tree, which if entirely one-sided is a essentially a linked list.
- Used to make **binary search trees**.
	- A binary tree that uses comparable keys to assign which direction a child is.
	- all nodes in the left tree are smaller
	- all nodes in the right tree are greater
	- There can be no duplicate node.
	- Because of the above it is more likely to be used as a data structure than a binary tree.
- **balanced BST**
  	- subtrees of any node are about the same height
- preorder traversal: root, left, right
- inorder: left, root, right
- postorder: left, right, root

#### Time Complexity:
- Indexing:  Binary Search Tree: O(log n)
- Search:    Binary Search Tree: O(log n)
- Insertion: Binary Search Tree: O(log n)





## Search Basics
### **Breadth First Search**
#### Definition:
- An algorithm that searches a tree (or graph) by searching levels of the tree first, starting at the root.
	- It finds every node on the same level, most often moving left to right.
	- While doing this it tracks the children nodes of the nodes on the current level.
	- When finished examining a level it moves to the left most node on the next level.
	- The bottom-right most node is evaluated last (the node that is deepest and is farthest right of it's level).
```
def bfs(v):
	q = [v]
	visited = {v}
	while q:
		curr = q.pop(0)
		if curr not in visited:
			visited.add(curr)
			for elem in curr.neighbors:
				q.append(elem)
```

#### What you need to know:
- Optimal for searching a tree that is wider than it is deep.
- Uses a queue to store information about the tree while it traverses a tree.
	- Because it uses a queue it is more memory intensive than **depth first search**.
	- The queue uses more memory because it needs to stores pointers
- in unweighted graphs it can be used to construct a shortest path from u to v.
#### Time Complexity:
- Search: Breadth First Search: O(|V| + |E|)


### **Depth First Search**
#### Definition:
- An algorithm that searches a tree (or graph) by searching depth of the tree first, starting at the root.
	- It traverses left down a tree until it cannot go further.
	- Once it reaches the end of a branch it traverses back up trying the right child of nodes on that branch, and if possible left from the right children.
	- When finished examining a branch it moves to the node right of the root then tries to go left on all it's children until it reaches the bottom.
	- The right most node is evaluated last (the node that is right of all it's ancestors).
```
def dfs(v):
	s = [v]
	visited = {v}
	while s:
		curr = s.pop()
		if curr not in visited:
			visited.add(curr)
			for elem in curr.neighbors:
				s.append(elem)
```

#### What you need to know:
- Optimal for searching a tree that is deeper than it is wide.
- Uses a stack to push nodes onto.
	- Because a stack is LIFO it does not need to keep track of the nodes pointers and is therefore less memory intensive than breadth first search.
	- Once it cannot go further left it begins evaluating the stack.
- topological sorting (i.e., resolving dependencies): the order in which a recursive DFS finishes processing the vertices of a (directed acyclic) graph of dependencies corresponds to a valid topological order.
#### Time Complexity:
- Search: Depth First Search: O(|E| + |V|)

#### Breadth First Search Vs. Depth First Search
- The simple answer to this question is that it depends on the size and shape of the tree.
  - For wide, shallow trees use Breadth First Search, or if the desired node closer to root
  - For deep, narrow trees use Depth First Search, or if desired node occur infrequently
- space: O(|V|)
- time: 
	- adjacency list: O(|V| + |E|)
	- adjacency matrix: O(|V|^2)

#### Nuances:
- Because BFS uses queues to store information about the nodes and its children, it could use more memory than is available on your computer. (But you probably won't have to worry about this.)
- If using a DFS on a tree that is very deep you might go unnecessarily deep in the search. See [xkcd](http://xkcd.com/761/) for more information.
- Breadth First Search tends to be a looping algorithm.
- Depth First Search tends to be a recursive algorithm.


## Efficient Sorting Basics
### **Insertion Sort**
- In each iteration, push arr[i] to its sorted position in arr[0..i], swap arr[i] with arr[i-1] if arr[i] < arr[i-1], then increase i
- stable: two equal values stay in the same relative position
```
def insertionSort(arr):
	for i in range(len(arr)):
		k = i
		while k > 0 and arr[k-1] > arr[k]:
			swap(arr, k-1, k)
			k -= 1
```

#### Time Complexity:
- Worst case: O(n^2), reverse-sorted input
- Best case: O(n), sorted input
- Average case: O(n^2)
- Space: O(1)

### **Selection Sort**
- Each iteration, swap min value of the latter section with arr[i]
- not stable
```
def selectionSort(arr):
	for i in range(len(arr)):
		m = index of min(arr[i:])
		swap(arr, i, m)
```

#### Time Complexity:
- Worst case: O(n^2)
- Best case: O(n^2)
- Average case: O(n^2)
- Space: O(1)

### **Merge Sort**
#### Definition:
- A comparison based sorting algorithm
  - Divides entire dataset into groups of at most two.
  - Compares each number one at a time, moving the smallest number to left of the pair.
  - Once all pairs sorted it then compares left most elements of the two leftmost pairs creating a sorted group of four with the smallest numbers on the left and the largest ones on the right.
  - This process is repeated until there is only one set.
```
def mergeSort(arr, h, t):
    if len(arr) < 2:
        return
	mid = (h + t) // 2
	mergeSort(arr, h, mid)
	mergeSort(arr, mid+1, t)
	merge(arr, h, mid, t)

def merge(arr, h, mid, t):
	left = arr[h:mid+1]
	right = arr[mid+1:t]
	i = j = 0
	k = h
	if left[i] < right[j]:
		arr[k] = left[i]
		i += 1
	else:
		arr[k] = right[j]
		j += 1
	k += 1
```
#### What you need to know:
- This is one of the most basic sorting algorithms.
- Know that it divides all the data into as small possible sets then compares them.

#### Time Complexity:
- Best Case Sort: O(nlogn)
	<!-- ```
	if (arr[mid] > arr[mid + 1]) 
		merge(arr, low, mid, high); 
	``` -->
- Average Case Sort: O(n log n)
- Worst Case Sort: O(n log n)
- Space: O(n)

### **Quicksort**
#### Definition:
- A comparison based sorting algorithm
  - Divides entire dataset in half by selecting the middle element and putting all smaller elements to the left of the element and larger ones to the right.
  - It repeats this process on the left side until it is comparing only two elements at which point the left side is sorted.
  - When the left side is finished sorting it performs the same operation on the right side.
- Computer architecture favors the quicksort process.
- good pivot value: median(arr[0], arr[-1], arr[n//2])
```
def quickSort(arr, h, t):
    if len(arr) < 2:
    	return;
    mid = partition(arr, h, t)
    quickSort(arr, h, mid-1)
    quickSort(arr, mid+1, t)
  
def partition(arr, h, t):
	pivot = h
	later = t
	while pivot < later:
		if arr[pivot+1] < arr[pivot]:
			swap(arr, pivot+1, pivot)
			pivot += 1
		else:
			swap(arr, pivot+1, later)
			later -= 1
	return pivot
```
```
 def partition(arr, low, high):
	i = low         # index of smaller element
	pivot = arr[high]     # pivot

	for j in range(low, high):
		# If current element is smaller than or
		# equal to pivot
		print(i, j, arr)
		if arr[j] <= pivot:
			
			arr[i], arr[j] = arr[j], arr[i]
			i = i+1

	arr[i], arr[high] = arr[high], arr[i]
	return i

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

```


#### What you need to know:
- While it has the same Big O as (or worse in some cases) many other sorting algorithms it is often faster in practice than many other sorting algorithms, such as merge sort.
- Know that it halves the data set by the average continuously until all the information is sorted.

#### Time Complexity:
- Best Case Sort: O(n log n), pivot always middle value, max depth O(log n)
- Average Case Sort: O(n log n)
- Worst Case Sort:  O(n^2), pivot always min/max value
- Space: O(log n)

### **Bubble Sort**
#### Definition:
- A comparison based sorting algorithm
	- It iterates left to right comparing every couplet, moving the smaller element to the left.
	- It repeats this process until it no longer moves an element to the left.

#### What you need to know:
- While it is very simple to implement, it is the least efficient of these three sorting methods.
- Know that it moves one space to the right comparing two elements at a time and moving the smaller on to left.

#### Time Complexity:
- Best Case Sort: Bubble Sort: O(n)
- Average Case Sort: Bubble Sort: O(n^2)
- Worst Case Sort: Bubble Sort: O(n^2)

#### Merge Sort Vs. Quicksort
- Quicksort is likely faster in practice.
- Merge Sort divides the set into the smallest possible groups immediately then reconstructs the incrementally as it sorts the groupings.
- Quicksort continually divides the set by the average, until the set is recursively sorted.
- Java.util.Arrays has a method sort(array)
	- primitives: quickSort
	- objects implementing Comparable: timSort (modified mergeSort)
- Merge Sort requires extra space, and Quick Sort is in place
- They both deploy the idea of divide-and-conquer. In merge sort, the divide step does hardly anything, and all the real work happens in the combine step. Quick Sort is the opposite: all the real work happens in the divide step. In fact, the combine step in Quick Sort does absolutely nothing.
- quicksort unstable, mergesort stable

### **Heap Sort**
- make the array into a max heap
- pull elements at the top, put it at the end of the array

### **Topological Sort**
- delete a vertex with indegree 0 will not remove any cycle
```
def topological_sort():
	k = 0
	while there is a node of indegree 0:
		label it as k
		delete it and all edges leaving it
		k += 1
```
-
```
def topological_sort(digraph):
    # digraph is a dictionary:
    #   key: a node
    # value: a set of adjacent neighboring nodes

    # construct a dictionary mapping nodes to their
    # indegrees
    indegrees = {node : 0 for node in digraph}
    for node in digraph:
        for neighbor in digraph[node]:
            indegrees[neighbor] += 1

    # track nodes with no incoming edges
    nodes_with_no_incoming_edges = []
    for node in digraph:
        if indegrees[node] == 0:
            nodes_with_no_incoming_edges.append(node)

    # initially, no nodes in our ordering
    topological_ordering = [] 
                
    # as long as there are nodes with no incoming edges
    # that can be added to the ordering 
    while len(nodes_with_no_incoming_edges) > 0:

        # add one of those nodes to the ordering
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)
    
        # decrement the indegree of that node's neighbors
        for neighbor in digraph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_incoming_edges.append(neighbor)

    # we've run out of nodes with no incoming edges
    # did we add all the nodes or find a cycle?
    if len(topological_ordering) == len(digraph):
        return topological_ordering  # got them all
    else:
        raise Exception("Graph has a cycle! No topological ordering exists.")
```
```
# Python program to print topological sorting of a DAG
from collections import defaultdict
class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list) # dictionary containing adjacency List
		self.V = vertices # No. of vertices

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A recursive function used by topologicalSort
	def topologicalSortUtil(self, v, visited, stack):

		# Mark the current node as visited.
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Push current vertex to stack which stores result
		stack.append(v)

	# The function to do Topological Sort. It uses recursive
	# topologicalSortUtil()
	def topologicalSort(self):
		# Mark all the vertices as not visited
		visited = [False]*self.V
		stack = []

		# Call the recursive helper function to store Topological
		# Sort starting from all vertices one by one
		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)

		# Print contents of the stack
		print(stack[::-1]) # return list in reverse order
```
### **Graph Coloring**
```
def color():
	for each vertex v in graph:
		c = find_color(v.neighbors)
		color v with c

def find_color(vs):
	used = [0] * (vs.length + 1)
	for v in vs:
		if v.color < len(used):
			used[v.color] += 1
	return smallest c such that used[c] == 0
```


## Basic Types of Algorithms
### **Recursive Algorithms**
#### Definition:
- An algorithm that calls itself in its definition.
	- **Recursive case** a conditional statement that is used to trigger the recursion.
	- **Base case** a conditional statement that is used to break the recursion.

#### What you need to know:
- **Stack level too deep** and **stack overflow**.
	- If you've seen either of these from a recursive algorithm, you messed up.
	- It means that your base case was never triggered because it was faulty or the problem was so massive you ran out of alloted memory.
	- Knowing whether or not you will reach a base case is integral to correctly using recursion.
	- Often used in Depth First Search


### **Iterative Algorithms**
#### Definition:
- An algorithm that is called repeatedly but for a finite number of times, each time being a single iteration.
  	- Often used to move incrementally through a data set.

#### What you need to know:
- Generally you will see iteration as loops, for, while, and until statements.
- Think of iteration as moving one at a time through a set.
- Often used to move through an array.

#### Recursion Vs. Iteration
- The differences between recursion and iteration can be confusing to distinguish since both can be used to implement the other. But know that,
	- Recursion is, usually, more expressive and easier to implement.
	- Iteration uses less memory.
- **Functional languages** tend to use recursion. (i.e. Haskell)
- **Imperative languages** tend to use iteration. (i.e. Ruby)
- Check out this [Stack Overflow post](http://stackoverflow.com/questions/19794739/what-is-the-difference-between-iteration-and-recursion) for more info.

#### Pseudo Code of Moving Through an Array (this is why iteration is used for this)
```
Recursion                         | Iteration
----------------------------------|----------------------------------
recursive method (array, n)       | iterative method (array)
  if array[n] is not nil          |   for n from 0 to size of array
    print array[n]                |     print(array[n])
    recursive method(array, n+1)  |
  else                            |
    exit loop                     |
```
### **Greedy Algorithm**
#### Definition:
- An algorithm that, while executing, selects only the information that meets a certain criteria.
- The general five components, taken from [Wikipedia](http://en.wikipedia.org/wiki/Greedy_algorithm#Specifics):
	- A candidate set, from which a solution is created.
	- A selection function, which chooses the best candidate to be added to the solution.
	- A feasibility function, that is used to determine if a candidate can be used to contribute to a solution.
	- An objective function, which assigns a value to a solution, or a partial solution.
	- A solution function, which will indicate when we have discovered a complete solution.

#### What you need to know:
- Used to find the expedient, though non-optimal, solution for a given problem.
- Generally used on sets of data where only a small proportion of the information evaluated meets the desired result.
- Often a greedy algorithm can help reduce the Big O of an algorithm.

#### Pseudo Code of a Greedy Algorithm to Find Largest Difference of any Two Numbers in an Array.
```
greedy algorithm (array)
	var largest difference = 0
	var new difference = find next difference (array[n], array[n+1])
	largest difference = new difference if new difference is > largest difference
	repeat above two steps until all differences have been found
	return largest difference
```

This algorithm never needed to compare all the differences to one another, saving it an entire iteration.

## Data structures in Python
- ``[]`` denotes optional arguments
- ``...`` means there are multiple such elements

### ** String**
- 
	```
	<str>  = <str>.strip()                       # Strips all whitespace characters from both ends.
	<str>  = <str>.strip('<chars>')              # Strips all passed characters from both ends.
	<list> = <str>.split()                       # Splits on one or more whitespace characters.
	<list> = <str>.split(sep=None, maxsplit=-1)  # Splits on 'sep' str at most 'maxsplit' times.
	<list> = <str>.splitlines(keepends=False)    # Splits on \n,\r,\r\n. Keeps them if 'keepends'.
	<str>  = <str>.join(<coll_of_strings>)       # Joins elements using string as separator.
	<bool> = <sub_str> in <str>                  # Checks if string contains a substring.
	<bool> = <str>.startswith(<sub_str>)         # Pass tuple of strings for multiple options.
	<bool> = <str>.endswith(<sub_str>)           # Pass tuple of strings for multiple options.
	<int>  = <str>.find(<sub_str>)               # Returns start index of first match or -1.
	<int>  = <str>.index(<sub_str>)              # Same but raises ValueError if missing.
	<str>  = <str>.replace(old, new [, count])   # Replaces 'old' with 'new' at most 'count' times.
	<str>  = <str>.translate(<table>)            # Use `str.maketrans(<dict>)` to generate table.
	<str>  = chr(<int>)                          # Converts int to Unicode char.
	<int>  = ord(<str>)                          # Converts Unicode char to int.   
	<str>.lower()								 # convert to lower case
	<str>.upper()								 # convert to upper case
	<str>.capitalize()							 # capitalize the first letter
	<str>.lstrip([<str>])
	<str>.rstrip([<str>])

	txt = ",,,,,ssaaww.....banana"
	x = txt.lstrip(",.asw")
	# 'banana'
	```

-
	┏━━━━━━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┯━━━━━━━━━━┓
	┃               │ [ !#$%…] │ [a-zA-Z] │  [¼½¾]   │  [²³¹]   │  [0-9]   ┃
	┠───────────────┼──────────┼──────────┼──────────┼──────────┼──────────┨
	┃ isprintable() │    ✓     │    ✓     │    ✓     │    ✓     │    ✓     ┃
	┃ isalnum()     │          │    ✓     │    ✓     │    ✓     │    ✓     ┃
	┃ isnumeric()   │          │          │    ✓     │    ✓     │    ✓     ┃
	┃ isdigit()     │          │          │          │    ✓     │    ✓     ┃
	┃ isdecimal()   │          │          │          │          │    ✓     ┃
	┗━━━━━━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┷━━━━━━━━━━┛

### **List**
#### Methods
- 
	```
	list.extend(iterable)		# Note that all iterable can be extended, not just list
	list.insert(i, x) 			# insert `x` at `i`
	list.remove(x) 				# remove the first occurrence of x, raise `ValueError` if not found
	list.pop([i]) 				# remove elem at `i`, remove the last item if argument unspecified
	list.popleft() 				# pop first elem in the queue
	list.index(x[, start[, end]]) # index of the first occurrence of `x`, raise `ValueError` if not found
	list.count(x) 				#returns # of x in the list
	list.sort(key = None, reverse = False) # sort in place
	list.reverse() 				#reverse in place
	reversed(list) 				# has return value, faster than arr[::-1]
	a = sorted(list, key=None, reverse=False)
	list.copy() 				# return shallow copy of the list, equivalent to a[:] 
	# Shallow Copy stores the references of objects to the original memory address.   
	lst[from_inclusive : to_exclusive : ±step_size]

	del arr[0]
	del arr[2:4]
	```

#### Miscellaneous
- could use list as stack or queue
- use it as queue not efficient, use `collections.deque` instead.
- list comprehensions
	- ``l = [(i, j) for i in x for j in y if i == j]``
- comparing sequences and other types: uses lexicographical ordering
- if one sequence is an initial sub-sequence of another, the shorter one is smaller
	```
	[1,2,3] < [1,2,4]
	[1,2,3,4] < [1,2,4]
	[1,2] < [1,2,3]
	```


### **Tuple & Sequences**
- tuples are immutable
- tuple may contain 1 or 0 items
	```
	empty_tuple = ()
	singleton = ('hi', )
	```
- tuple unpacking: ``x, y, z = ('hi', 'hello', 'hey')``


### **Set**
```
d = {} #this creates empty dict
s = set() 

# remove element from set, raise error if does not exist
s.remove("test")

# remove but doesn't raise error
s.discard(elem)

# put letters in a string to a set
letters = set('arabica')

# elems in a not in b
a - b

# elems in a or b
a | b

# elems in both a and b
a & b
a.intersection(b)

# symmetric difference: elems in a or b but not in both
a ^ b

# set comprehension
a = {x for x in set1 if x not in set2}

# looping
s = {1,2,3,4}
for elem in sorted(s):
	...

# subset
<bool> = s1.issubset(s2)    
s1 <= s2

# superset
<bool> = s1.issuperset(s2)    
s1 >= s2
```

### **Frozen set**
- ``frozenset([iterable])`` immutable version of set
- can be used as keys in dictionary, or elements of another set


### **Dictionary**
- keys has to be immutable
```
d = {'qwE': 20, 'vk': 22}

# could use the del keyword to delete key:value pair
del d['qwE']

# returns list of all keys
list(d)

# sort keys in ascending order
sorted(d)

# use 'in' to check if contains a key
's' in d

# Adds items. Replaces ones with matching keys.
d1.update(d2)

# constructs dictionary from sequences of key-value pairs
# could put list of tuples as argument
dict([('qwe', 20), ('vk', 22)])

# dict comprehension
{x: x**2 for x in range(4)}

# looping
for k, v in d.items():
	...

for elem in d.keys()/d.values():

# print all keys
''.join(d.keys())

# return None if key does not exist
d.get("test")

# return default value if key does not exist
d.get("test2", default_value)

# delete one element, and also return the value
d.pop("test")

```




### **Collections**
- starts with ``from collections import xxx``

#### deque (double-ended queue)
- ``collections.dequec([iterable[, maxlen]])`` returns a deque object initialized left-to-right (using `append()` with data from iterable). Empty if iterable not specified
- supports thread-safe, memory efficient `append`s & `pop`s from either side, O(1) performance
- whereas `list` is optimized for fast **fixed-length** operations, has O(n) costs for `pop(0)` and `insert(0, v)`, which change size & position of the underlyding data representation
```
q = deque([1,2,3,4])
q.append(5)
q.appendleft(x)
q.popleft()
q.pop()
q.remove(x) #remove first occurrence of x, raise ValueError if not found
q.count(x) # counter number of deque elements equal to x
q.extend(iterable) #extend the RHS of deque
q.extendleft(iterable) #extend the LHS of the deque, will reverse the elements in iterable
```

#### Counter
- support convenient tallies
- different fron dict: returns a zero count for missing items, instead of raising a `KeyError`
- **methods**
	- ``collections.Counter([iterable/mapping])``
		```
		c = Counter('hellohiheyyy')
		c = Counter(lst)
		c = Counter(dict)

		#remove elem entirely from counter
		del c['qwE']
		# does not remove, counter entry still has a 0 count
		c['qwE'] = 0
		```
	- ``elements()`` return an iterator over elements repeating as many times as its count
		````
		sorted(c.elements())
		#[1,1,1,2,2,3]
		````
	- ``most_common([n])`` return list of n most common elements and their counts; if n omitted then returns all
	- ``subtract([iterable/mapping])``
		```
		# c, d are two counters
		c.subtract(d)
		```
- examples
	```
	# sum of all counts
	sum(c.values())

	# list unique elements
	list(c)

	# convert to set/dict
	set(c)
	dict(c)

	# k least common elements
	c.most_common()[::-1][k]

	# mathematical operations are provided for combining Counter objects
	c = Counter(a=3, b=1)
	d = Counter(a=1, b=2)

	c + d # Counter({'a':4, 'b':3})

	# keep only positive counts
	c - d # Counter({'a':2})

	# intersection / take min over all elems
	c & d # Counter({'a':1, 'b':1})

	# union / max over all elems
	c | d # Counter({'a':3, 'b':2})
	```

#### defaultDict
- if a key encountered for the first time, an entry automatically created
```
d = defaultdict(list)
for k, v in pairs:
	d[k].append(v)

# Creates a dict with default value 1.
d = defaultdict(lambda: 1) 
```

#### OrderedDict
- preserves the order in which the keys are inserted
- but built-in dict class remeber insertion order now (from Python 3.7)
- could used in LRU cache
- if value of a certain key changed, position of that key remains unchanged
- deleting and re-inserting push the key to the end
- ``popitem(last=True)`` returns and removes a key:value pair, popped in LIFO order if last=True, FIFO otherwise
- ``move_to_end(key, last=True)`` move an existing key to either end of the dict, moved to the right end if last=True, raise `KeyError` if key not in dict
- LRU cache
	```
	from collections import OrderedDict 

	class LRUCache: 
		# initialising capacity 
		def __init__(self, capacity: int): 
			self.cache = OrderedDict() 
			self.capacity = capacity 
	
		# we return the value of the key 
		# that is queried in O(1) and return -1 if we 
		# don't find the key in out dict / cache. 
		# And also move the key to the end 
		# to show that it was recently used. 
		def get(self, key: int) -> int: 
			if key not in self.cache: 
				return -1
			else: 
				self.cache.move_to_end(key) 
				return self.cache[key] 
	
		# first, we add / update the key by conventional methods. 
		# And also move the key to the end to show that it was recently used. 
		# But here we will also check whether the length of our 
		# ordered dictionary has exceeded our capacity, 
		# If so we remove the first key (least recently used) 
		def put(self, key: int, value: int) -> None: 
			self.cache[key] = value ack
			self.cache.move_to_end(key) 
			if len(self.cache) > self.capacity: 
				self.cache.popitem(last = False) 
	
	```

### **itertools**
#### itertools.combinations
- ``combinations(iterable, r)`` return r length subsequences of elements from iterable
- inputs treated as unique based on their position, not value
- returns \frac{n!}{r!(n-r)!} items
- 
	```
	combinations('ABCD', 2)  # --> AB AC AD BC BD CD
	combinations(range(4), 3)  # --> 012 013 023 123

	letters = 'abcdef'
	comb = combinations(letters, 3)
	#select 3 from letters
	y = [''.join(c) for c in comb]
	```
- ``combinations_with_replacement(iterable, r)`` allow individual elements to be repeated more than once
- returns \frac{(n+r-1)!}{r!(n-1)!} items
	```
	list(combinations_with_replacement(range(1, 5), 2))
	# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
	```
 
- implementation
	```
	def combinations(lst, r):
		if r == 1:
			return [(item, ) for item in lst]
		n = len(lst)
		res = []
		for i in range(n):
			rest = lst[i+1:]
			# rest = lst[i:] if with replacement
			prev = combinations(rest, r-1)
			prev = [(lst[i],) + item for item in prev]
			res += prev
		return res
	```
#### itertools.permutations
- ``permutations(iterable[, r])`` return successive r length permutations of elements in the iterable
- returns \frac{n!}{r!} items
-
	```
	permutations([1,2,3])
	# (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

	permutations([1,2,3], 2)
	# (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
	```
- implementation
	```
	def permutation(lst, r=None):
		if not r:
			r = len(lst)
		if r == 1:
			return [(item, ) for item in lst]
		n = len(lst)
		res = []
		for i in range(n):
			rest = lst[:i] + lst[i+1:]
			prev = permutation(rest, r-1)
			prev = [(lst[i],) + item for item in prev]
			res += prev
		return res
	```

#### itertools.product
- ``product(*iterables[, repeat])`` return the cartesian product of input iterables
- `product(A, B)` is the same as `[(x, y) for x in A for y in B]`, but not ``for x, y in zip(A, B)``
- `*iterables` could be a list of lists, need to add `*` prior to the variable name
- To compute the product of an iterable with itself, specify the number of repetitions with the optional repeat keyword argument. 
- For example, product(A, repeat=4) means the same as product(A, A, A, A).
- 
	```
	arr1 = [1,2,3]
	arr2 = [5,6,7]
	product(arr1, arr2)
	# [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
	```
- 
	```
	def product(lst, r=None):
		if r:
			lst = [lst for _ in range(r)]
		if len(lst) == 1:
			print(lst)
			return [(e,) for e in lst[0]]

		temp = lst[:-1]
		prev = product(temp)
		res = []
		for p in prev:
			for r in lst[-1]:
				res.append(p + (r,))
		return res

	```

#### itertools.groupby
- ``groupby(iterable[, key])`` returns consecutive keys and groups from the iterable, key is a function that calculates keys for each elem in the iterable
- 
	```
	L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)] 
	key_func = lambda x: x[0] 
	
	for key, group in groupby(L, key_func): 
		print(key + " :", list(group)) 

	# a : [('a', 1), ('a', 2)]
	# b : [('b', 3), ('b', 4)]


	for key, group in groupby([1,1,1,1,5,1,1,1,1,4]):
		print(key, list(group))
	# 1 [1, 1, 1, 1]
	# 5 [5]
	# 1 [1, 1, 1, 1]
	# 4 [4]
	lst = [1,1,2,2,2,3,3,1]
	groupby(lst)
	#[(1, 2), (2, 3), (3, 2), (1, 1)]
	```

#### other methods
- **accumulate**
	- ``itertools.accumulate(iterable[, func, *, initial=None])``
	- Make an iterator that returns accumulated sums, or accumulated results of other binary functions
	- 
		```
		data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
		list(accumulate(data, operator.mul))     # running product
		# [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
		list(accumulate(data, max))              # running maximum
		# [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
		```
- **chain** 
	- Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. 
	- Used for treating consecutive sequences as a single sequence.
	- ``itertools.chain(*iterables)``
		- ``chain('ABC', 'DEF')`` --> A B C D E F
		- 
			```
			def chain(*iterables):
				# chain('ABC', 'DEF') --> A B C D E F
				for it in iterables:
					for element in it:
						yield element
			```
	- ``chain.from_iterable(iterable)``
		- Alternate constructor for chain(). 
		- Gets chained inputs from a single iterable argument that is evaluated lazily.
		-  ``chain.from_iterable(['ABC', 'DEF'])`` --> A B C D E F

### Generators / Iterators
- Any function that contains a yield statement returns a generator.
- e.g.
	```
	def count(start, step):
		while True:
			yield start
			start += step

	counter = count(10, 2)
	next(counter), next(counter), next(counter)
	# (10, 12, 14)

	```

### **heapq (minheap)**
- every parent node has a value less than or equal to any of its children
-  `import heap`
- `heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]`
- methods
	- `import heapq`
	- `heapify(x)` transform list x into a heap, **in-place**, O(n)
	- `heapq.heappush(heap, item)`
	- `heappop(heap)` pop and return the smallest item from the heap. Raise `IndexError` if heap empty
	- `heap[0]` access the smallest element without popping it
	- `nlargest(n, iterable, key=None)` return a list with n largest elements from the iterable
	- `nsmallest(n, iterable, key=None)` return smallest n elements
	- `heapq.heappushpop(heap, 2)` push then pop
	- `heapq.heapreplace(li, 4)` pop then push

- could define ``__lt__`` method to compare objects
	```
	def __lt__(self, other):
		return self.intAttribute < other.intAttribute
	```
- or use tuples and heapq sort by the first and subsequent elements
	
- Examples
	```
	import heapq
	h = []
	heappush(h, 5)
	heappush(h, 4)
	a = heappop(h)
	```

### **built-in functions**
- ``abs()``
- ``all(iterable)`` returns True if all elements in the iterable are true, or iterable empty
- ``any(iterable)`` returns True if any elem in the iterable true
- ``ascii(object)`` returns a string containing a printable representation fo an object, escape non-ASCII characters
- ``enumerate(iterable, start = 0)`` returns a list of tuples of index paired with each item in the iterable
- ``eval(expression)``
	```
	x = 1
	eval('x+1')
	eval('1+2+3')
	```
- ``isinstance(object, classinfo)`` return True if the object is an instance of the classinfo
	- e.g. ``isinstabce(1, int)``
- ``map(function, iterable, ...)`` return an iterator that applies function to every item of iterable
	```
	nums = [1,2,3,4]
	doubled_nums = list(map(lambda x: x + x, nums))
	```
- ``pow(base, exp[, mod])`` return base^pow; if mod present, return base^power%mod
- ``round(number[, ndigits])`` return number rounded to ndigits after the decimal point; if ndigits omitted or is None, return the nearest integer
- ``set(iterable)``
- ``sorted(iterable, *, key = None, reverse = False)``
- ``str(object)``
- ``var([object])`` return the `__dict__` attribute of object
	```
	class Fool:
		def __init__(self, name='qwE', age='20'):
			self.name = name
			self.age = age
	me = Fool()
	print(vars(me)) #{'name': 'qwE', 'age': 20}
	```
- ``zip(iterables)`` make an iterator that aggregates elements from each of the iterables
	```
	zip('abcd', 'xy') #ax, by
	```
- ``object.__dict__``
- ``instance.__class__`` the class of that instance
- ``definition.__name__`` the name of the class, function, method, ...


## common algs
### **Trie node**
- 
	```
	class Trie:
		def __init__(self, val=None):
			self.val = val
			self.char_map = {}
			
		def insert(self, word, move):
			if len(word) == 0:
				self.char_map['<END>'] = Trie(move)
			else:
				if word[0] not in self.char_map:
					self.char_map[word[0]] = Trie()
				self.char_map[word[0]].insert(word[1:], move)
				
		def is_str(self, node):
			if '<END>' in node.char_map:
				return node.char_map['<END>'].val
			return None
		
		def traverse(self, node, char):
			if char in node.char_map:
				return node.char_map[char]
			return None
	```
	```
	class TrieNode():
		def __init__(self):
			self.children = collections.defaultdict(TrieNode)
			self.is_word = False
			
		def __repr__(self):
			def recur(node, indent):
				return "".join(indent + key + ("$" if child.is_word else "") 
									+ recur(child, indent + "  ") 
					for key, child in node.children.items())

			return recur(self, "\n")

	class WordDictionary:
		def __init__(self):
			"""
			Initialize your data structure here.
			"""
			self.root = TrieNode()        
			

		def addWord(self, word: str) -> None:
			"""
			Adds a word into the data structure.
			"""
			curr = self.root
			for w in word:
				curr = curr.children[w]   
			curr.is_word = True
	

		def search(self, word: str) -> bool:
			"""
			Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
			""" 
			self.res = False
			self.dfs(self.root, word)
			return self.res

		def dfs(self, node, word):
			if not word:
				if node.is_word:
					self.res = True
				return
			if word[0] == '.':
				for nxt in node.children.values():
					self.dfs(nxt, word[1:])
			else:
				if word[0] not in node.children:
					return
				self.dfs(node.children[word[0]], word[1:])
        
	```
- Insert and search costs O(key_length)
- the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N), where N is number of keys in Trie
- backtracking algorithm, find all paths from one node to another
	```
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def backtrack(node, path):
            if node == n-1:
                res.append(path)
            
            for nxt in graph[node]:
                if nxt not in path:
                    backtrack(nxt, path + [nxt])
        backtrack(0, [0])
        return res
	```


### **functools**


### **math**
- types
	```
	<int>      = int(<float/str/bool>)       # Or: math.floor(<float>)
	<float>    = float(<int/str/bool>)       # Or: <real>e±<int>
	<complex>  = complex(real=0, imag=0)     # Or: <real> ± <real>j
	<Fraction> = fractions.Fraction(0, 1)    # Or: Fraction(numerator=0, denominator=1)
	<Decimal>  = decimal.Decimal(<str/int>)  # Or: Decimal((sign, digits, exponent))

	
	```
- Note that 
	- 'int(<str>)' and 'float(<str>)' raise ValueError on malformed strings.
	- Decimal numbers can be represented exactly, unlike floats where '1.1 + 2.2 != 3.3'.
	- Precision of decimal operations is set with: 'decimal.getcontext().prec = <int>'.

- basic functions
	```
	<num> = pow(<num>, <num>)                # Or: <num> ** <num>
	<num> = abs(<num>)                       # <float> = abs(<complex>)
	<num> = round(<num> [, ±ndigits])        # `round(126, -1) == 130`
	```
- math
	```
	from math import e, pi, inf, nan, isinf, isnan
	from math import cos, acos, sin, asin, tan, atan, degrees, radians
	from math import log, log10, log2
	```
	- print(float('Inf') - float('Inf')) # nan

- bitwise operators
	- a = int(a, 2) convert to from a binary sting '11' to int 3
	- 
		```
		>>> bin(10)
		'0b1010'
		>>> 0b1010
		10
		```
	- 
		```
		<int> = <int> & <int>                    # And
		<int> = <int> | <int>                    # Or
		<int> = <int> ^ <int>                    # Xor (0 if both bits equal)
		<int> = <int> << n_bits                  # Shift left (>> for right)
		<int> = ~<int>                           # Not (also: -<int> - 1)
		```
	- ``(int) <<`` shift bits, e.g. ``carry = (x & y) << 1``
	- ``^`` XOR in binary
	- ``~`` flip all bits in binary and add 1 at front / add 1 to the number, e.g. `~24 = -25`
	- ``&`` AND in binary
	- ``|`` OR in binary
### **Other tricks**
- conditions can be chained: ``a < b == c``
- String.isdigit()
- initialize 2d array: dp = [[0 for i in range(n+1)] for j in range(n)]
- dp: if have multiple inputs (e.g. 2+ strings matching), use 2d array
- `math.ceil()` round to the next greatest int
- binary search: do iterative instead of recursive version
	```
	l, r = 1, ...
	while l < r:
		...
		if ... :
			l = mid + 1
		else:
			r = mid - 1

	return l
	```
	- while loop板子有3个
		- 当你需要找一个特定值left <= right, left = mid + 1, right = mid - 1;
			- 
			```
			int l = 0, r = nums.length - 1;
			while (l <= r) {
		        int mid = l + (r-l) / 2;
		        if (arr[mid] == target)  {
		            return mid;
		        } else if (arr[mid] > target) {
		            r = mid - 1;
		        } else {
		            l = mid + 1;
		        }
			}
			```
		- 找下界（第一次出现）left + 1 < right, left = mid, right = mid;
			- if this number not in list, return its upper index
			- e.g. arr = [1,2,3,4,6], target = 5, return 4
			- 
			```
			int l = 0, r = nums.length - 1;
			while (l < r) {
			    int mid = l + (r-l) / 2;
			    if (nums[mid] >= target) {
			        // 满足条件的时候，把右边界设成mid，这样右边不断向**近，直到第一次出现
			        r = mid;
			    } else {
			        // 不满足的时候，移动左边
			        l = mid + 1;
			    }
			}
			```
		- 找上界（最后一次出现）left < right, left = mid + 1, right = mid;
			- if this number not in list, return its lower index
			- e.g. arr = [1,2,3,4,6], target = 5, return 3
			- 
			```
			int l = 0, r = nums.length - 1;
			while (l < r) {
			    // 注意！向右逼近的时候， mid 后面要+1，不然会死循环
				int mid = (l + r)//2;
			    if (nums[mid] <= target) {
			        // 满足条件的时候，把左边界设成mid，这样不断向右逼近，直到最后一次出现
			        l = mid;
			    } else {
			        // 不满足的时候，移动右边
			        r = mid - 1;
			    }
			}
			```
	- 
- `div, mod = divmod(num, divisor)`
- valid parenthesis: if encounter ')' and if stack and stack[-1] == '(', pop the last '('
- `string.lower()` convert to lower case
- `string.isupper()`, `string.islower()`, `string.upper()`
- when using zip(a, b) and a b have different lengths, could not iterate through all possible combinations
- common data structure to use: hashmap, 1/2 queue(s), stack, minheap/maxheap, doubly linked list
- 2 deque for keeping max and min
	```
	for num in nums:
		while maxd and maxd[-1] < num:
			maxd.pop()
		while mind and mind[-1] > num:
			mind.pop()
		maxd.append(num)
		mind.append(num)
	```


- `s = s.replace(" ", "")` remove whitespace in s
- use stack
- `idx ^= 1` flip the `idx` between 0 and 1
- ``chr(int)`` convert int to char, 
- ``ord(char)`` convert char to int, ord('a') = 97
- ``str.isdigit()`` check if a string only contains numeric values
- ``str.isalpha()`` returns True if all the characters are alphabet letters (a-z).
- random number generation
	- ``random.randrange(start, stop[, step])`` return a randomly selected element from range(start, stop, step). 
	- ``random.randint(a, b)`` return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
	- ``random.choice(seq)`` return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
	- ``random.random()`` generate a random number between 0 and 1 
- ``gcd(a, b)``
- ``string.split()`` split by white space
- ``'a' <= c <= 'z'`` string comparison
- ``str.find(sub,start,end)`` returns the lowest index of the substring if it is found in given string. If not found then it returns -1.
- ``min(list, key = ...)`` find the min element in a list by key
- ``yield``
	- The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
	- ```
	# A Python program to generate squares from 1 
	# to 100 using yield and therefore generator 
	# An infinite generator function that prints 
	# next square number. It starts with 1 
	def nextSquare(): 
		i = 1; 
	
		# An Infinite loop to generate squares  
		while True: 
			yield i*i                 
			i += 1  # Next execution resumes  
					# from this point      
	
	# Driver code to test above generator  
	# function 
	for num in nextSquare(): 
		if num > 100: 
			break    
		print(num) 
	```
- binary numbers
	```
	>>> bin(6)  
	'0b110'
	>>> '{0:08b}'.format(6)
	'00000110'
	```
- `dictionary.get(keyname, [value])` value is optional, returned if the specified key does not exist.
- `bisect`
	- bisect.bisect_left(a, x, lo=0, hi=len(a))
		- Locate the insertion point for x in a to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered; 
	- bisect.bisect(a, x, lo=0, hi=len(a))
		- Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a.
		- The returned insertion point i partitions the array a into two halves so that all(val <= x for val in a[lo:i]) for the left side and all(val > x for val in a[i:hi]) for the right side.
- `float('inf')`, `float('-inf')` positive and negative infinity
- assign values at odd and even indices
	```
	res[::2] = [x for _ in range((m+1)//2)]
	res[1::2] = [y for _ in range(m//2)]
	```

- maximal int
	- math.inf

Default value None
todo:
add more from algo: dp, greedy
leetcode tricks
sorting优缺点
OOP problem
memoization
python constructor
functools
numpy

## 3410
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=216941&highlight=two%2Bsigma
latency vs throughput
thread vs process

## random links
- https://www.evernote.com/shard/s576/client/snv?noteGuid=7e58b450-1abe-43a8-bf82-fbf07f1db13c&noteKey=049802174415b418a2e65f75b744ab72&sn=https%3A%2F%2Fwww.evernote.com%2Fshard%2Fs576%2Fsh%2F7e58b450-1abe-43a8-bf82-fbf07f1db13c%2F049802174415b418a2e65f75b744ab72&title=Interview%2BPreparation
- comprehensive python cheatsheet 
https://gto76.github.io/python-cheatsheet/