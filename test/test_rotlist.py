import rotlist

l = [2, 4, 5, 6, 7, 10, 12, 13, 20]


def test_find_sorted_unique():
    for i, n in enumerate(l):
        assert i == rotlist.find_sortedunique(l, n)


def test_non_existing_values_sorted_unique():
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value


def rotate(l, rotations):
    return l[rotations:] + l[:rotations]


def test_find_sorted_unique_rotated():
    for n in l:
        print(n)
        for r in range(len(l)):
            print(r)
            rl = rotate(l, r)
            i = rotlist.find_sorteduniquerotated(rl, n)
            try:
                assert n == rl[i]
            except:
                print(n)


def test_non_existing_values_rotated():
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value


def test_repeated():
    l = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 2, 3, 8, 8]
    i = rotlist.find_sorteduniquerotated(l, 1)
    assert 1 == l[i]
