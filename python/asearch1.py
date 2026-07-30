# Graph
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
    'J': []
}

# Heuristic
def heuristic(n):
    h = {
        'A': 11, 'B': 6, 'C': 5, 'D': 7,
        'E': 3, 'F': 6, 'G': 5, 'H': 3,
        'I': 1, 'J': 0
    }
    return h[n]

# A* Algorithm
def a_star(start, goal):
    open_list = [start]
    closed_list = []

    g = {start: 0}
    parent = {start: None}

    while open_list:
        # node with lowest f(n)
        n = min(open_list, key=lambda x: g[x] + heuristic(x))

        # goal check
        if n == goal:
            path = []
            while n is not None:
                path.append(n)
                n = parent[n]
            path.reverse()
            print("Path found:", path)
            return

        open_list.remove(n)
        closed_list.append(n)

        # explore neighbors
        for (m, cost) in graph[n]:
            new_cost = g[n] + cost

            if m not in open_list and m not in closed_list:
                open_list.append(m)
                parent[m] = n
                g[m] = new_cost

            elif new_cost < g.get(m, float('inf')):
                g[m] = new_cost
                parent[m] = n
                if m in closed_list:
                    closed_list.remove(m)
                    open_list.append(m)

    print("No path found")

# Run
a_star('A', 'J')