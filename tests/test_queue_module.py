import random
from queue import PriorityQueue
from string import ascii_uppercase as symbols

import pytest
from pytest import mark


def get_elements(nro):
    return ["".join(random.choices(symbols, k=3)) for _ in range(nro)]


def test_put_and_then_get_item():
    max_elements = 10_000

    numbers = [i for i in range(max_elements)]
    random.shuffle(numbers)

    pqueue = PriorityQueue()

    for n in numbers:
        key = "".join(random.choices(symbols, k=5))
        pqueue.put((n, key))

    before = -1
    while not pqueue.empty():
        value, _ = pqueue.get()
        if not (before < value):
            raise ValueError("falhouuuuu!!")
        before = value


def test_priority_queue_has_no_len_attribute():
    max_elements = 10_000

    numbers = [i for i in range(max_elements)]
    random.shuffle(numbers)

    pqueue = PriorityQueue()

    for n in numbers:
        key = "".join(random.choices(symbols, k=5))
        pqueue.put((n, key))

    with pytest.raises(TypeError):
        assert len(pqueue) == max_elements


@mark.parametrize("quantity", [10_000, 100_000, 500_000])
def test_random_insertion(quantity):
    elements = get_elements(quantity)
    weights = [i for i in range(quantity)]
    random.shuffle(weights)

    pq = PriorityQueue()
    for w, e in zip(weights, elements):
        pq.put((w, e))

    before = -1
    while not pq.empty():
        value, _ = pq.get()
        if value < before:
            raise RuntimeError()
        before = value


@mark.parametrize("quantity", [10_000, 100_000, 500_000])
def test_decreasing_insertion(quantity):
    elements = get_elements(quantity)
    weights = [i for i in range(quantity)]
    weights = sorted(weights, reverse=True)

    pq = PriorityQueue()
    for w, e in zip(weights, elements):
        pq.put((w, e))

    before = -1
    while not pq.empty():
        value, _ = pq.get()
        if value < before:
            raise RuntimeError()
        before = value
