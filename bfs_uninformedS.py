from collections import deque
def bfs(graph, start, goal):
    visited = set([start])
    queue = deque([[start]])
    traversal_order = []
    while queue:
        path = queue.popleft()
        node = path[-1]
        traversal_order.append(node)
        if node == goal:
            print("BFS Traversal Order:", " -> ".join(traversal_order))
            print("Shortest Path:", " -> ".join(path))
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    print("BFS Traversal Order:", " -> ".join(traversal_order))
    print("No path found")
# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A', 'F')
