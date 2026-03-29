from kruskal import kruskal, is_connected
edges = [(0,1,4),(0,2,2),(1,2,1),(1,3,5),(2,3,3)]
mst, total = kruskal(4, edges)
assert total == 6  # edges: (1,2,1), (0,2,2), (2,3,3)
assert len(mst) == 3
assert is_connected(4, edges)
# Disconnected graph
assert not is_connected(4, [(0,1,1)])
# Single node
mst2, total2 = kruskal(1, [])
assert total2 == 0 and len(mst2) == 0
print("kruskal tests passed")
