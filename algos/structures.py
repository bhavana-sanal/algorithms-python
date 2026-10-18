from collections import OrderedDict


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def _walk(self, s):
        node = self.root
        for ch in s:
            node = node.get(ch)
            if node is None:
                return None
        return node

    def contains(self, word):
        n = self._walk(word)
        return bool(n and "$" in n)

    def with_prefix(self, prefix):
        out = []

        def dfs(node, acc):
            for ch, nxt in node.items():
                if ch == "$":
                    out.append(acc)
                else:
                    dfs(nxt, acc + ch)

        n = self._walk(prefix)
        if n:
            dfs(n, prefix)
        return sorted(out)


class UnionFind:
    def __init__(self, n):
        self.p, self.size = list(range(n)), [1] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.p[b] = a
        self.size[a] += self.size[b]
        return True


class LRUCache:
    def __init__(self, capacity):
        self.cap, self.d = capacity, OrderedDict()

    def get(self, k, default=None):
        if k not in self.d:
            return default
        self.d.move_to_end(k)
        return self.d[k]

    def put(self, k, v):
        self.d[k] = v
        self.d.move_to_end(k)
        if len(self.d) > self.cap:
            self.d.popitem(last=False)
