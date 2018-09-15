import rotlist

l = [2, 4, 5, 6, 7, 10, 12]


def test_sortedunique():
    for i, n in enumerate(l):
        assert i == rotlist.find_sortedunique(l, n)


def test_non_existing_values():
    assert rotlist.find_sortedunique(l, 1) is None  # Find small non existing value
    assert rotlist.find_sortedunique(l, 100) is None  # Find big non existing value
