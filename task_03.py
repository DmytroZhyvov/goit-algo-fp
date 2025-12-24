import heapq


def create_weighted_graph():
    """Create a dictionary-based weighted graph"""
    nodes = [
        "Palais Royal-Musee du Louvre",
        "Toledo Station",
        "T-Centralen",
        "Khalid Bin Al Waleed",
        "Olaias",
        "Westfriedhof",
        "Zoloti Vorota",
        "Formosa Boulevard Station",
    ]

    weights = {
        ("Palais Royal-Musee du Louvre", "Toledo Station"): 2,
        ("Palais Royal-Musee du Louvre", "T-Centralen"): 3,
        ("Palais Royal-Musee du Louvre", "Khalid Bin Al Waleed"): 4,
        ("Toledo Station", "Olaias"): 5,
        ("T-Centralen", "Olaias"): 2,
        ("T-Centralen", "Westfriedhof"): 4,
        ("Olaias", "Zoloti Vorota"): 3,
        ("Khalid Bin Al Waleed", "Zoloti Vorota"): 6,
        ("Westfriedhof", "Formosa Boulevard Station"): 5,
        ("Zoloti Vorota", "Formosa Boulevard Station"): 2,
    }

    graph = {node: {} for node in nodes}

    for (u, v), w in weights.items():
        graph[u][v] = w
        graph[v][u] = w

    return graph


def dijkstra(graph, start):
    """Dijkstra algorithm using a binary heap"""

    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


if __name__ == "__main__":
    graph = create_weighted_graph()

    print("\n***Dijkstra shortest paths (binary heap) ***")

    start = "Palais Royal-Musee du Louvre"
    distances = dijkstra(graph, start)

    print(f"\nShortest distances from '{start}':")
    for target, dist in distances.items():
        print(f"  to {target}: {dist}")
