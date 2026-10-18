import random, re
import pytest
from algos import *

rng = random.Random(0)


def test_sorts_match_builtin():
    for _ in range(50):
        a = [rng.randint(0, 50) for _ in range(rng.randint(0, 40))]
        for f in (merge_sort, quick_sort, heap_sort, counting_sort):
            assert f(a) == sorted(a), f.__name__


def test_search():
    a = sorted(rng.sample(range(1000), 100))
    assert all(binary_search(a, x) == i for i, x in enumerate(a)) and binary_search(a, -5) == -1
    b = [rng.randint(0, 30) for _ in range(60)]
    assert all(quickselect(b, k) == sorted(b)[k] for k in range(60))


def test_graphs():
    g = {"a": [("b", 1), ("c", 4)], "b": [("c", 2), ("d", 6)], "c": [("d", 3)]}
    assert dijkstra(g, "a") == {"a": 0, "b": 1, "c": 3, "d": 6}
    assert bfs_shortest_path({1: [2, 3], 2: [4], 3: [4]}, 1, 4) in ([1, 2, 4], [1, 3, 4])
    assert astar_grid([[0, 0, 0], [1, 1, 0], [0, 0, 0]], (0, 0), (2, 0)) == 6
    assert astar_grid([[0, 1], [1, 0]], (0, 0), (1, 1)) == -1
    order = topological_sort({"a": ["b"], "b": ["c"], "c": []})
    assert order == ["a", "b", "c"]
    with pytest.raises(ValueError):
        topological_sort({"a": ["b"], "b": ["a"]})
    assert kruskal(4, [(1, 0, 1), (2, 1, 2), (3, 0, 2), (4, 2, 3)])[0] == 7


def test_dp():
    assert lcs("AGGTAB", "GXTXAYB") == "GTAB"
    assert edit_distance("kitten", "sitting") == 3
    assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert coin_change([1, 5, 10, 25], 63) == 6 and coin_change([2], 3) == -1


def test_structures_and_strings():
    t = Trie()
    for w in ["car", "card", "care", "dog"]:
        t.insert(w)
    assert t.contains("car") and not t.contains("ca") and t.with_prefix("car") == ["car", "card", "care"]
    c = LRUCache(2); c.put(1, 1); c.put(2, 2); c.get(1); c.put(3, 3)
    assert c.get(2) is None and c.get(1) == 1
    for _ in range(100):
        s = "".join(rng.choice("ab") for _ in range(30)); p = "".join(rng.choice("ab") for _ in range(3))
        assert kmp_search(s, p) == [m.start() for m in re.finditer(f"(?={p})", s)]
