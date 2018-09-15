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
