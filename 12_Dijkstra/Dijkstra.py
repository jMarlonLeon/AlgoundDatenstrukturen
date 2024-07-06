
# Dijkstra-Algorithmus
# Der Dijkstra-Algorithmus ist ein Algorithmus zur Bestimmung des kürzesten Weges 
# von einem Startknoten zu allen anderen Knoten in einem gewichteten Graphen.

# Der Algorithmus arbeitet wie folgt:
# 1. Initialisiere alle Knoten mit unendlichem Abstand zum Startknoten und den Startknoten mit 0.
# 2. Wähle den Knoten mit dem geringsten Abstand zum Startknoten.
# 3. Aktualisiere die Abstände zu den Nachbarknoten des gewählten Knotens.
# 4. Markiere den gewählten Knoten als besucht.
# 5. Wiederhole Schritte 2-4, bis alle Knoten besucht wurden.

import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
    
    def add_edge(self, from_node, to_node, distance):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
    
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        pq = [(0, start)]
        previous = {node: None for node in self.nodes}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.edges[current_node]:
                distance = current_distance + self.distances[(current_node, neighbor)]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return distances, previous

# Beispiel zur Verwendung der Graphenklasse
if __name__ == "__main__":
    graph = Graph()
    
    # Füge Kanten zum Graphen hinzu
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 6)
    graph.add_edge('E', 'F', 3)

    # Führe den Dijkstra-Algorithmus aus
    start_node = 'A'
    distances, previous = graph.dijkstra(start_node)

    # Gib die Ergebnisse aus
    print(f"Kürzeste Distanzen von Knoten {start_node}:")
    for node, distance in distances.items():
        print(f"{node}: {distance}")

    print("\nKürzeste Pfade:")
    for node in graph.nodes:
        if node != start_node:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            print(f"{start_node} -> {node}: {' -> '.join(path)}")