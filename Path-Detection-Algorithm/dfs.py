#Depth-First Search
#Works partially
#The commented code prints and takes the nodes twice.
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

#The following code does not account for parents more than once but moves through all the child

def dfs(node):
    visited.append(node)
    stack.append(node)

    while stack:
        parent = stack.pop()
        #stack.append(parent)
        for child in graph[parent]:
            if child not in visited:
                visited.append(child)
                stack.append(child)
                print(stack)
                return dfs(child)
        #stack.pop()
        print(parent)

print("The DFS Algoritm is :")
dfs('A')