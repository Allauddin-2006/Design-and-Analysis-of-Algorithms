from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


if __name__ == "__main__":
    # Sample graph represented as an adjacency list
    # Graph structure:
    #      A
    #     / \
    #    B   C
    #   / \   \
    #  D   E   F
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    start = 'A'
    result = bfs(graph, start)

    print(f"Starting Node: {start}")
    print("BFS Traversal Order: " + " -> ".join(result))
