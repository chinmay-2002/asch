import collections

def bfs(graph, root):
    visited = []
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft() # remove front element
        visited.append(vertex) # add at end
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i) # added at rear
                
    print(visited)
 
graph = {
    1:[2,3], # no of connected edges
    2:[4,5,6],
    3:[4,5],
    4:[6],
    5:[3,2],
    6:[4,1]
 }
# graph is visualized through dictionary data structure in python
bfs(graph, 3)









'''
if you wanna add edges dynamically


def add_edge(graph, vertex):
    num_edges = int(input(f"Enter the number of connected edges for vertex {vertex}: "))
    edges = []
    
    for i in range(num_edges):
        connected_vertex = int(input(f"Enter the connected vertex {i+1} for vertex {vertex}: "))
        edges.append(connected_vertex)
    
    graph[vertex] = edges

# Example usage
graph = {}

# Adding edges dynamically
num_vertices = int(input("Enter the number of vertices: "))
for i in range(1, num_vertices + 1):
    add_edge(graph, i)

# Print the updated graph
print(graph)



'''