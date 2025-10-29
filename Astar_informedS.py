from queue import PriorityQueue
# Graph with costs
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}
# Heuristic estimates (h)
heuristic = {'A': 6, 'B': 4, 'C': 2, 'D': 4, 'E': 1, 'F': 0}
def path_cost(graph, path):
    """Calculate total g-cost of a given path."""
    return sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
def a_star(graph, start, goal, heuristic):
    """Perform A* search and print traversal details."""
    open_list = PriorityQueue()
    open_list.put((0, [start]))
    visited = set()
    print("\nA* Search Traversal:\n" + "-"*30)
    while not open_list.empty():
        f, path = open_list.get()
        node = path[-1]
        print(f"Visited: {node}, Path: {'->'.join(path)}, f={f}")
        if node == goal:
            print("\nGoal Reached!")
            return path
        if node not in visited:
            visited.add(node)
            g = path_cost(graph, path)
            for neighbor, cost in graph[node].items():
                if neighbor not in visited:
                    f_new = g + cost + heuristic[neighbor]
                    open_list.put((f_new, path + [neighbor]))
    return None
# Run A* Search
start, goal = 'A', 'F'
final_path = a_star(graph, start, goal, heuristic)
# Display Final Result
if final_path:
    print(f"\nShortest Path: {' -> '.join(final_path)}")
else:
    print("\nNo path found!")
