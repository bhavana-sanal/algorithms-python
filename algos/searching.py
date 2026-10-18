import random


def binary_search(a, x):
    """Index of x in sorted list a, or -1."""
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        lo, hi = (mid + 1, hi) if a[mid] < x else (lo, mid - 1)
    return -1


def quickselect(a, k):
    """k-th smallest element (0-indexed) in expected O(n)."""
    p = random.choice(a)
    lo, eq = [x for x in a if x < p], [x for x in a if x == p]
    if k < len(lo):
        return quickselect(lo, k)
    if k < len(lo) + len(eq):
        return p
    return quickselect([x for x in a if x > p], k - len(lo) - len(eq))
