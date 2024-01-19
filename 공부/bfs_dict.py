def bfs(start_node, graph):
    queue = list()
    visited = list()
    
    if start_node in graph:
        queue.append(start_node)   
        while queue:
            start_node = queue.pop(0)
            visited.append(start_node)
            for node in graph[start_node]:
                if node not in queue:
                    queue.append(node)
    else:
        return -1
    return visited
    


def solution():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(bfs('B',graph))

solution()
