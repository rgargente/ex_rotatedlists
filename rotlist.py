def find_sortedunique(l, n):
    def get_middle(min, max):
        return int(min + (max - min) / 2)

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


def find_sorteduniquerotated(l, n):
    def get_middle(min, max):
        return int(min + (max - min) / 2)

    min = 0
    max = len(l) - 1
    i = 0
    while min < max:
        i_set = False
        value = l[i]
        if value == n:
            return i
        if l[0] < value:  # still sorted, smaller values can be to the right, never to the left
            if n < l[min] or value < n:  # if our number is smaller than the beginning or bigger that the current one, we can discard the left size now
                min = i + 1
            else:
                if min > 0:
                    i = get_middle(min, i)  # let's just search to the left
                else:
                    i = get_middle(1, i)  # let's just search to the left
                i_set = True
        elif i > 0:  # pass the rotation point, bigger values can be to the left
            if n < value:  # if our number is smaller than the current value, it must be to the left
                max = i - 1
            else:  # otherwise, if it wasn't the current one, let's just discard it
                min = i + 1

        if not i_set:
            i = get_middle(min, max)

    return i if l[i] == n else None
