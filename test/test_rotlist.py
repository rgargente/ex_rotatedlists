import random

import pytest

import rotlist

l = [2, 4, 5, 6, 7, 10, 12, 13, 20]


def rotate(l, rotations):
    return l[rotations:] + l[:rotations]


def test_find_sorted_unique():
    for i, n in enumerate(l):
        assert i == rotlist.find_sortedunique(l, n)


def test_non_existing_values_sorted_unique():
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value


def _test_all_values_and_rotations(l):
    prev_n = None
    for n in l:
        if n != prev_n:
            prev_n = n
            for r in range(len(l)):
                rl = rotate(l, r)
                i = rotlist.find_sorted_nonunique_rotated(rl, n)
                assert n == rl[i]


def test_find_sorted_nonunique_rotated_with_unique_list():
    _test_all_values_and_rotations(l)


def test_non_existing_values_rotated():
    rl = rotate(l, 4)
    assert rotlist.find_sortedunique(rl, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(rl, 100) is None  # Find big non existing value


def test_repeated():
    l = [7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 2, 3]
    i = rotlist.find_sorted_nonunique_rotated(l, 1)
    assert 1 == l[i]


def test_repeated_difficult():
    l = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 2, 3, 8, 8]
    i = rotlist.find_sorted_nonunique_rotated(l, 1)
    assert 1 == l[i]

    l = [8, 8, 8, 1, 2, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    i = rotlist.find_sorted_nonunique_rotated(l, 1)
    assert 1 == l[i]


def test_non_existing_values_difficult():
    l = [8, 8, 8, 2, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value
    l = [8] * 10
    assert rotlist.find_sortedunique(l, 1) is None  # Find a non existing value where all values are the same


def get_random_sorted_repeated_list(size):
    n = random.randint(0, 100)
    l = [n]
    for i in range(size - 1):
        if random.random() > .7:
            n += random.randint(1, 10)
        l.append(n)
    return l


@pytest.mark.repeat(100)
@pytest.mark.timeout(1)
def test_long_random_repeated_list():
    size = 100
    l = get_random_sorted_repeated_list(size)
    print(l)

    # test all positions of one rotation
    rl = rotate(l, random.randint(1, size))
    prev_n = None
    for n in rl:
        if n != prev_n:
            prev_n = n
            i = rotlist.find_sorted_nonunique_rotated(rl, n)
            assert n == rl[i]

    # test all rotations for one number
    n = l[0]
    for r in range(size):
        rl = rotate(l, r)
        i = rotlist.find_sorted_nonunique_rotated(rl, n)
        assert n == rl[i]
