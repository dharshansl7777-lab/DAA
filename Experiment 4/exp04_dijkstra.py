import heapq


def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """

    n = len(graph)

    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]  # (distance, vertex)
    visited = set()

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):
    path = []

    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


def main():

    # Graph represented as an adjacency list
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }

    source = 0

    dist, prev = dijkstra(graph, source)

    print(f"Shortest Paths from Vertex {source}")
    print("-" * 55)
    print(f"{'Vertex':<10}{'Distance':<12}{'Path'}")

    for vertex in range(len(graph)):
        path = reconstruct_path(prev, source, vertex)

        if path:
            path_str = " -> ".join(map(str, path))
        else:
            path_str = "No Path"

        distance = dist[vertex]
        if distance == float('inf'):
            distance = "INF"

        print(f"{vertex:<10}{distance!s:<12}{path_str}")


if __name__ == "__main__":
    main()
