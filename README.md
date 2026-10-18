# algorithms-python

[![CI](https://github.com/bhavana-sanal/algorithms-python/actions/workflows/ci.yml/badge.svg)](https://github.com/bhavana-sanal/algorithms-python/actions) ![License](https://img.shields.io/badge/license-MIT-blue)

Clean, tested implementations of core algorithms and data structures in pure Python (stdlib only).

| Area | Contents |
|---|---|
| Sorting | merge, quick (random pivot), heap, counting |
| Searching | binary search, quickselect (expected O(n)) |
| Graphs | Dijkstra, BFS shortest path, A\* on grids, topological sort (Kahn), Kruskal MST |
| Dynamic programming | LCS, edit distance, 0/1 knapsack, LIS in O(n log n), coin change |
| Data structures | Trie, Union-Find (path compression + union by size), LRU cache |
| Strings | Knuth–Morris–Pratt search |

```bash
pip install pytest && pytest
```
Sorting and string search are checked against Python's built-ins/`re` on random inputs.
