graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "F"],
    "C": ["A", "E"],
    "D": ["B", "I"],
    "E": ["C", "F", "G"],
    "F": ["B", "E", "G"],
    "G": ["F", "K"],
    "I": ["K"],
    "K": ["I", "G"],
}

visited = []
queue = []


def bfs(graph, visited, node):
    visited.append(node)
    queue.append(node)

    while queue:
        # print(queue)
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(graph, visited, "A")
