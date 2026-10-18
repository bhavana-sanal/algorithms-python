import heapq
import random


def merge_sort(a):
    if len(a) <= 1:
        return list(a)
    l, r = merge_sort(a[: len(a) // 2]), merge_sort(a[len(a) // 2:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    return out + l[i:] + r[j:]


def quick_sort(a):
    if len(a) <= 1:
        return list(a)
    p = random.choice(a)
    return quick_sort([x for x in a if x < p]) + [x for x in a if x == p] + quick_sort([x for x in a if x > p])


def heap_sort(a):
    h = list(a)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def counting_sort(a):
    """O(n + k) sort for non-negative integers."""
    if not a:
        return []
    c = [0] * (max(a) + 1)
    for x in a:
        c[x] += 1
    return [i for i, n in enumerate(c) for _ in range(n)]
