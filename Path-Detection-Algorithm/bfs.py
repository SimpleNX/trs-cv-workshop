#Breadth-First Search
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

visited = []
queue=[]


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue :
        m = queue.pop(0)
        
        #visited.append(m) By this method the queue starts containing nodes which have been visited.
        #This would cause queue to have multiple entries and the search will start to take more time.
        #From the outputs, by appending the pop key here, and not later we check the child nodes, more than once.

        print(m, end =' ')

        for neighbour in graph[m]:
            if neighbour not in visited :
                visited.append(neighbour)
                queue.append(neighbour)
        #print(visited)
        #print(queue)

print("The BFS Algorithm is:")
bfs(visited, graph, 'A')
