from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                new = list(state)
                new[zero], new[r*3+c] = new[r*3+c], new[zero]

                queue.append((tuple(new), path + [state]))

    return None


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = bfs(start, goal)

print("Solution Steps:")

for i, state in enumerate(solution):
    print("Step", i)
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()