#!/usr/bin/env python3
"""Kruskal minimum spanning tree. Zero dependencies."""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
        return True

def kruskal(n, edges):
    """edges: list of (u, v, weight). Returns MST edges and total weight."""
    edges_sorted = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    mst = []
    total = 0
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1: break
    return mst, total

def is_connected(n, edges):
    uf = UnionFind(n)
    for u, v, _ in edges: uf.union(u, v)
    roots = set(uf.find(i) for i in range(n))
    return len(roots) == 1

if __name__ == "__main__":
    edges = [(0,1,4),(0,2,2),(1,2,1),(1,3,5),(2,3,3)]
    mst, total = kruskal(4, edges)
    print(f"MST: {mst}, total weight: {total}")
