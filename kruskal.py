#!/usr/bin/env python3
"""Kruskal's MST. Input: 'src dst weight' per line."""
import sys
edges, nodes = [], set()
for line in sys.stdin:
    p=line.split()
    if len(p)>=3: edges.append((float(p[2]),p[0],p[1])); nodes.update(p[:2])
parent = {n:n for n in nodes}; rank = {n:0 for n in nodes}
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a==b: return False
    if rank[a]<rank[b]: a,b=b,a
    parent[b]=a
    if rank[a]==rank[b]: rank[a]+=1
    return True
edges.sort(); mst, total = [], 0
for w,u,v in edges:
    if union(u,v): mst.append((u,v,w)); total+=w
print(f"MST total weight: {total}")
for u,v,w in mst: print(f"  {u} -- {v} (weight {w})")
