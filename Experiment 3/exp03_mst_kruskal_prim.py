import heapq


# ---------- Union-Find for Kruskal ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


# ---------- Kruskal Algorithm ----------
def kruskal(n, edges):
    edges.sort()

    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


# ---------- Prim Algorithm ----------
def prim(n, graph, start=0):

    visited = [False] * n

    priority_queue = [(0, start, -1)]

    mst = []
    total_cost = 0

    while priority_queue:

        weight, current, parent = heapq.heappop(priority_queue)

        if visited[current]:
            continue

        visited[current] = True

        if parent != -1:
            mst.append((parent, current, weight))
            total_cost += weight

        for neighbor, edge_weight in graph[current]:
            if not visited[neighbor]:
                heapq.heappush(priority_queue,
                               (edge_weight, neighbor, current))

    return mst, total_cost


# ---------- Main ----------
def main():

    n = 7

    edges = [
        (7, 0, 1),
        (5, 0, 3),
        (8, 1, 2),
        (9, 1, 3),
        (7, 1, 4),
        (5, 2, 4),
        (15, 3, 4),
        (6, 3, 5),
        (8, 4, 5),
        (9, 4, 6),
        (11, 5, 6)
    ]

    graph = {i: [] for i in range(n)}

    for w, u, v in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    mst1, cost1 = kruskal(n, edges.copy())

    print("===== Kruskal's Algorithm =====")

    for u, v, w in mst1:
        print(f"{u} -- {v}  Weight = {w}")

    print("Total Cost =", cost1)

    print()

    mst2, cost2 = prim(n, graph)

    print("===== Prim's Algorithm =====")

    for u, v, w in mst2:
        print(f"{u} -- {v}  Weight = {w}")

    print("Total Cost =", cost2)


if __name__ == "__main__":
    main()
