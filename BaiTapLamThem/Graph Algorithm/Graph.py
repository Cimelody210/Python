def BFS(graph, start, end):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        visited.add(node)
        if node == end:
            return True
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
    return False
graph = {
    
    # Lười edit chỗ này
    "A": ["B","C"],
    "A": ["B","C"],
    "A": ["B","C"],
    "A": ["B","C"],
    "A": ["B","C"],
    "A": [],
}
print(BFS(graph, "A", "F"))
# => True