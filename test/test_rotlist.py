import rotlist
import pytest

l = [2, 4, 5, 6, 7, 10, 12, 13, 20]


def rotate(l, rotations):
    return l[rotations:] + l[:rotations]


def test_find_sorted_unique():
    for i, n in enumerate(l):
        assert i == rotlist.find_sortedunique(l, n)


def test_non_existing_values_sorted_unique():
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value


def test_find_sorted_nonunique_rotated_with_unique_list():
    for n in l:
        for r in range(len(l)):
            rl = rotate(l, r)
            i = rotlist.find_sorted_nonunique_rotated(rl, n)
            assert n == rl[i]



def test_non_existing_values_rotated():
    rl = rotate(l, 4)
    assert rotlist.find_sortedunique(rl, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(rl, 100) is None  # Find big non existing value


def test_repeated():
    l = [7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 2, 3]
    i = rotlist.find_sorted_nonunique_rotated(l, 1)
    assert 1 == l[i]


def test_repeated_hardcase():
    l = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 2, 3, 8, 8]
    i = rotlist.find_sorted_nonunique_rotated(l, 1)
    assert 1 == l[i]

    l = [8, 8, 8, 1, 2, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    i = rotlist.find_sorted_nonunique_rotated(l, 1)
    assert 1 == l[i]


def test_non_existing_values_hardcase():
    l = [8, 8, 8, 2, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value
    l = [8] * 10
    assert rotlist.find_sortedunique(l, 1) is None  # Find a non existing value where all values are the same
