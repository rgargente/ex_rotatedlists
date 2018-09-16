def get_middle(min, max):
    return int(min + (max - min) / 2)


def find_sortedunique(l, n):
    min = 0
    max = len(l) - 1
    i = 0
    while min < max:
        if l[i] == n:
            return i
        if n < l[i]:
            max = i - 1
        elif l[i] < n:
            min = i + 1
        i = get_middle(min, max)

    return i if l[i] == n else None


def find_sorted_nonunique_rotated(l, n):
    def find_first_different(l, repeated_i):
        """
        At this moment I think it's better to go the easiest way and just do a sequential search.
        The binary searh is faster because we know something about the data, therefore we can discard big chunks of data.
        In this case however we just don't know anything. We could try to do some kind of binary search, going left
        first and then right, then looking in the gaps. However, in practice it'd be as fast as searching in random places
        until the number is found. I don't think there is any reason to think that random is faster or better than
        sequential. On top of it, sequential is definitely simpler!
        """
        diff_i = None
        repeated_v = l[repeated_i]
        for i, v in enumerate(l[1:]):  # Skip the first element
            if v != repeated_v:
                diff_i = i + 1  # +1 because we skipped the first element
                break
        return diff_i

    min = 0
    max = len(l) - 1
    i = 0
    while min < max:
        prev_i = i

        value = l[i]
        if value == n:
            return i

        if l[0] < value:  # still sorted, smaller values can be to the right, never to the left
            if n < l[min] or value < n:
                # if our number is smaller than the beginning or bigger that the current one,
                # we can discard the left size now
                min = i + 1
            else:  # let's just search to the left
                i = get_middle(min, i)
        elif i > 0:
            if l[0] == value and min == 0:  # still  a repeated value, we've learned nothing
                i = find_first_different(l, i)
            else:  # pass the rotation point, bigger values can be to the left
                if n < value:  # if our number is smaller than the current value, it must be to the left...
                    max = i - 1
                elif l[0] > n:
                    # ...if it's bigger, it has to be to the right if the first element was already bigger than n
                    min = i + 1
                else:  # we don't know which side it is, let's just search to the left
                    i = get_middle(min, i)

        if prev_i == i:
            # if so far we haven't modified i (i.e. we don't want to search somewhere specific),
            # let's find the new middle
            i = get_middle(min, max)
            if prev_i == i: # it's possible that the middle returns the same value we already had when max-min==1 ...
                i += 1 # ... in that case, let's try the next value this time

    return i if l[i] == n else None
