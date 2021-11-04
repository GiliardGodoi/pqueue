import random
from queue import PriorityQueue
from string import ascii_uppercase as symbols

import pytest


def test_put_and_then_get_item():
    max_elements = 10_000

    numbers = [i for i in range(max_elements) ]
    random.shuffle(numbers)

    pqueue = PriorityQueue()

    for n in numbers:
        key = ''.join(random.choices(symbols, k=5))
        pqueue.put((n, key))

    before = -1
    while not pqueue.empty():
        value, _ = pqueue.get()
        if not (before < value):
            raise ValueError("falhouuuuu!!")
        before = value

def test_priority_queue_has_no_len_attribute():
    max_elements = 10_000

    numbers = [i for i in range(max_elements) ]
    random.shuffle(numbers)

    pqueue = PriorityQueue()

    for n in numbers:
        key = ''.join(random.choices(symbols, k=5))
        pqueue.put((n, key))

    with pytest.raises(TypeError):
        assert len(pqueue) == max_elements
