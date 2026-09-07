from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print("Visited:", node)

        # Check if goal is found
        if node == goal:
            print("\nGoal node", goal, "found!")
            return

        # Add unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("\nGoal node", goal, "not found!")

# Start node and Goal node
start = 'A'
goal = 'D'

bfs(graph, start, goal)