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
        i_set = False
        value = l[i]
        if value == n:
            return i

        if l[0] < value:  # still sorted, smaller values can be to the right, never to the left
            if n < l[min] or value < n:
                # if our number is smaller than the beginning or bigger that the current one, we can discard the left size now
                min = i + 1
            else:  # let's just search to the left
                if min > 0:
                    i = get_middle(min, i)
                else:
                    i = get_middle(1, i)
                i_set = True
        elif i > 0:
            if l[0] == value:  # still  a repeated value, we've learned nothing
                i = find_first_different(l, i)
                i_set = True
            else:  # pass the rotation point, bigger values can be to the left
                if n < value:  # if our number is smaller than the current value, it must be to the left...
                    max = i - 1
                elif l[
                    0] > n:  # ...if it's bigger, it has to be to the right if the first element was already bigger than n
                    min = i + 1
                else:  # we don't know which side it is, let's just search to the left
                    i = get_middle(min, i)
                    i_set = True

        if not i_set:
            i = get_middle(min, max)

    return i if l[i] == n else None
