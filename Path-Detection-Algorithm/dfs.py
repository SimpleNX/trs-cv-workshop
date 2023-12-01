#Depth-First Search
#Works
graph = {
    'A' : ['B','D'],
    'B' : ['A','C'],
    'C' : ['B'],
    'D' : ['A','E','H'],
    'E' : ['D','F'],
    'F' : ['E'],
    'G' : ['H'],
    'H' : ['D','G']
}

visited =[]
stack = []

def dfs(node):
    if node not in visited :
        visited.append(node)
        stack.append(node)

    while stack:
        parent = stack.pop()
        stack.append(parent)
        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
                print(stack)
                return dfs(child)
        stack.pop()
        print(parent)

print("The DFS Algoritm is :")
dfs('A')