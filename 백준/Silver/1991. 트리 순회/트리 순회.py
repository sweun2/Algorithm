n = int(input())
graph = [[] for _ in range(26)]
for _ in range(n):
    p, c1, c2 = input().split()
    idx = ord(p) - 65
    graph[idx] = [c1, c2]

def preorder(node):
    if node != ".":
        result.append(node)
        preorder(graph[ord(node) - 65][0])
        preorder(graph[ord(node) - 65][1])

result = []
preorder('A')
print("".join(result))

def inorder(node):
    if node != ".":
        inorder(graph[ord(node) - 65][0])
        result.append(node)
        inorder(graph[ord(node) - 65][1])

result = []
inorder('A')
print("".join(result))

def postorder(node):
    if node != ".":
        postorder(graph[ord(node) - 65][0])
        postorder(graph[ord(node) - 65][1])
        result.append(node)

result = []
postorder('A')
print("".join(result))
