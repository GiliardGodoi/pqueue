import random
from itertools import product
from string import ascii_uppercase as symbols

from pqueue import PQueue
from pytest import mark, fixture


@fixture
def pq():
    pq = PQueue()

    pq.push(100, 'AQT')
    pq.push(49, 'BWD')
    pq.push(302, 'YUP')

    return pq


def get_elements(nro):
    return [ ''.join(random.choices(symbols, k=3)) for _ in range(nro)]

def test_insert_the_same_element_twice(pq):

    pq.push(27, 'AQT')

    assert len(pq) == 3

    value, item = pq.pop()
    assert item == 'AQT'
    assert value == 27

    value, item = pq.pop()
    assert item == 'BWD'
    assert value == 49

    value, item = pq.pop()
    assert item == 'YUP'
    assert value == 302

    assert pq.empty()


def test_bool_method(pq):
    blocker = 0
    while pq:
        _, _ = pq.pop()
        blocker += 1
        if blocker > 4:
            raise RuntimeError("while do not stop!")

def test_contains_method(pq):
    assert 'BWD' in pq
    assert not ('GWT' in pq)

def test_len_method(pq):
    expected = 3
    while pq:
        assert len(pq) == expected
        _, _ = pq.pop()
        expected -= 1

@mark.parametrize(
    'quantity',
    [10_000, 100_000, 500_000]
)
def test_random_insertion(quantity):
    elements = get_elements(quantity)
    weights = [ i for i in range(quantity)]
    random.shuffle(weights)

    pq = PQueue()
    for w, e in zip(weights, elements):
        pq.push(w, e)

    before = -1
    while not pq.empty():
        value, _ = pq.pop()
        if value < before:
            raise RuntimeError()
        before = value

@mark.parametrize(
    'quantity',
    [10_000, 100_000, 500_000]
)
def test_decreasing_insertion(quantity):
    elements = get_elements(quantity)
    weights = [ i for i in range(quantity)]
    weights = sorted(weights, reverse=True)

    pq = PQueue()
    for w, e in zip(weights, elements):
        pq.push(w, e)

    before = -1
    while not pq.empty():
        value, _ = pq.pop()
        if value < before:
            raise RuntimeError()
        before = value
