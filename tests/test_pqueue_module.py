import random
from itertools import product
from string import ascii_uppercase as symbols

from pqueue import PQueue
from pytest import fixture


@fixture
def pq():
    pq = PQueue()

    pq.push(100, 'AQT')
    pq.push(49, 'BWD')
    pq.push(302, 'YUP')

    return pq

@fixture
def elements():
    return [ ''.join(e) for e in product(symbols, repeat=3)]

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

def test_random_insertion(elements):
    weights = [ i for i in range(len(elements))]
    random.shuffle(weights)

    pq = PQueue()
    for w, e in zip(weights, elements):
        pq.push(w, e)

    before = -1
    while pq:
        value, _ = pq.pop()
        if value < before:
            raise RuntimeError()
        before = value

def test_decreasing_insertion(elements):
    weights = [ i for i in range(len(elements))]
    weights = sorted(weights, reverse=True)

    pq = PQueue()
    for w, e in zip(weights, elements):
        pq.push(w, e)

    before = -1
    while pq:
        value, _ = pq.pop()
        if value < before:
            raise RuntimeError()
        before = value
