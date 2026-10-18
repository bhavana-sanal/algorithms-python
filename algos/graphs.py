import heapq
from collections import deque


def dijkstra(graph, src):
    """graph: {u: [(v, weight), ...]} with non-negative weights. Returns {node: distance}."""
    dist, pq = {src: 0}, [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, []):
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w
                heapq.heappush(pq, (d + w, v))
    return dist


def bfs_shortest_path(graph, src, dst):
    prev, q = {src: None}, deque([src])
    while q:
        u = q.popleft()
        if u == dst:
            path = []
            while u is not None:
                path.append(u); u = prev[u]
            return path[::-1]
        for v in graph.get(u, []):
            if v not in prev:
                prev[v] = u; q.append(v)
    return None


def astar_grid(grid, start, goal):
    """4-connected A* on a grid of 0 (free) / 1 (wall) with Manhattan heuristic. Returns path length or -1."""
    h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])
    best, pq = {start: 0}, [(h(start), 0, start)]
    while pq:
        _, g, (r, c) = heapq.heappop(pq)
        if (r, c) == goal:
            return g
        if g > best[(r, c)]:
            continue
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not grid[nr][nc] and g + 1 < best.get((nr, nc), 1e18):
                best[(nr, nc)] = g + 1
                heapq.heappush(pq, (g + 1 + h((nr, nc)), g + 1, (nr, nc)))
    return -1


def topological_sort(graph):
    """Kahn's algorithm. graph: {u: [v, ...]}. Raises ValueError on a cycle."""
    indeg = {u: 0 for u in graph}
    for vs in graph.values():
        for v in vs:
            indeg[v] = indeg.get(v, 0) + 1
    q, order = deque(u for u, d in indeg.items() if d == 0), []
    while q:
        u = q.popleft(); order.append(u)
        for v in graph.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != len(indeg):
        raise ValueError("graph has a cycle")
    return order


def kruskal(n, edges):
    """Minimum spanning tree. edges: [(w, u, v)]. Returns (total_weight, chosen_edges)."""
    from .structures import UnionFind
    uf, total, chosen = UnionFind(n), 0, []
    for w, u, v in sorted(edges):
        if uf.union(u, v):
            total += w; chosen.append((w, u, v))
    return total, chosen
