import heapq

def dijkstra(graph, start):
    # Inisialisasi semua jarak ke ∞, kecuali simpul awal (0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue untuk pemrosesan simpul
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

# ===== INPUT MANUAL =====
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

# Input simpul awal
start_node = input("\nMasukkan simpul awal untuk Dijkstra: ").strip()

# ===== JALANKAN DIJKSTRA =====
result = dijkstra(graph, start_node)

# ===== TAMPILKAN HASIL =====
print("\nHasil Akhir Jarak Minimum dari Simpul", start_node, ":\n")
for node in sorted(graph.keys()):
    distance = result.get(node, float('inf'))
    if distance == float('inf'):
        print(f"{start_node} → {node} : ∞ (tidak dapat dijangkau)")
    else:
        print(f"{start_node} → {node} : {distance}")
