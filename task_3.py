import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))

    def dijkstra(self, start):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        distances = {vertex: float('inf') for vertex in self.edges}
        for i in self.edges:
            for j, _ in self.edges[i]:
                if j not in distances:
                    distances[j] = float('inf')
        distances[start] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 6)
    graph.add_edge('C', 'D', 3)

    start_vertex = 'A'
    shortest_paths = graph.dijkstra(start_vertex)
    print(f"Shortest paths from {start_vertex}: {shortest_paths}")
