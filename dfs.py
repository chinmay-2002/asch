visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        visited.add(root)
        print(root)
        for i in graph[root]:
            print("AB Yaha neighbour is ", i)
            dfs(visited, graph, i)
            print("Mai hogaya bhai ", i)
    
    
graph = {
    1:[2,3], # no of connected edges
    2:[4,5,6],
    3:[4,5],
    4:[6],
    5:[3,2],
    6:[4,1]
}

dfs(visited, graph, 1)