# pqueue

Just toying around with a priority queue implementation using heapq.

There is a built-in priority queue classe implemented in Python, and it can be accessed as:

```python
from queue import PriorityQueue

pq = PriorityQueue()

pq.put((10, 'ABC'))
pq.put((6, 'ZXY'))

value, label = pq.get()
```

For another example, look up for ```test_queue_module.py``` in the folder ```tests```.

The implementation proposed here uses the ```heapq``` module underneath. Some covinient methods are also proposed, for instance:

- __bool__ method instead using ```.empty()``` in ```while``` clauses
- __len__ method to access the quantity of elements in the queue
- __contains__ to verify if an element belong to the queue
- ```push``` insert an elements
- ```pop``` return the minimum element
