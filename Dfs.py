def dfs(graph, start, goal):
    visited = []
    stack = []

    stack.append(start)
    visited.append(start)

    print('The path traversed is:')

    while stack:
        element = stack.pop()
        print(element, " ")

        if element == goal:
            break

        for neighbor in graph[element]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(neighbor)


# A dictionary representing the graph
graph = {
    'A': ['C', 'B'],
    'B': ['E', 'D'],
    'C': ['G', 'F'],
    'D': [],
    'E': ['I', 'H'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

start = 'A'
goal = 'J'

dfs(graph, start, goal)