#Depth-First Search
#Assignment
#Works partially
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
stack = ['A']

def dfs(node):
    visited.append(node)
    stack.append(node)

    while stack:
        parent = stack.pop()
        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
                return dfs(child)
        print(parent)

print("The DFS Algoritm is :")
dfs('A')