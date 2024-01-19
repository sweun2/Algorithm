com_cnt = int(input())
edge_cnt =int(input())

visited = list()
queue = list()
graph = [list() for i in range(com_cnt+1)]
for i in range(edge_cnt):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in graph[1]:
    queue.append(node)
node = 1
visited.append(1)

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
    for j in graph[node]:
        if j not in visited and j not in queue:
            queue.append(j)