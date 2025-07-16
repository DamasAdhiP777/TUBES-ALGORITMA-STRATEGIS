import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {}
nodes = input("Masukkan semua simpul :").split()

for node in nodes:
    connections = []
    n_edges = int(input(f"Berapa banyak tetangga dari simpul '{node}'? "))
    for _ in range(n_edges):
        neighbor = input(f"  → Nama simpul tetangga dari '{node}': ").strip()
        weight = int(input(f"    Jarak dari '{node}' ke '{neighbor}': "))
        connections.append((neighbor, weight))
    graph[node] = connections

start_node = input("\nMasukkan simpul awal untuk Dijkstra: ").strip()

result = dijkstra(graph, start_node)

print("\n======================================")
print("Nama  : Damas Adhi Prasetyo")
print("NIM   : 23533777")
print("Kelas : 4D")
print("======================================")
print("\nItem yang diambil (berat, profit):")
print("\nHasil Akhir Jarak Minimum dari Simpul", start_node, ":\n")
for node in sorted(graph.keys()):
    distance = result.get(node, float('inf'))
    if distance == float('inf'):
        print(f"{start_node} → {node} : ∞ (tidak dapat dijangkau)")
    else:
        print(f"{start_node} → {node} : {distance}")
