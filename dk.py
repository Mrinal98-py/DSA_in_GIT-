import heapq

def dijkstra(graph, start):
    # Priority queue to store the minimum distance to each node
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    # Dictionary to store the shortest path to each node
    shortest_path = {node: float('inf') for node in graph}
    shortest_path[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the distance is greater than the already found shortest distance, skip
        if current_distance > shortest_path[current_node]:
            continue
        
        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_path

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")
