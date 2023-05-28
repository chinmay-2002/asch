#Prims 

import sys
def prim_mst(graph):
    
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices
    parent = [None] * num_vertices
    mst_set = [False] * num_vertices
    key[0] = 0
    
    for _ in range(num_vertices):
        
        u = minimum_key(key, mst_set)
        mst_set[u] = True
        
        for v in range(num_vertices):
            if graph[u][v] > 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
                
    print("Edge\tweight")

    for i in range(1, num_vertices):
        print(f"{parent[i]} - {i}  \t{graph[i][parent[i]]}")
                
def minimum_key(key, mst_set):
    min_key = sys.maxsize
    min_index = -1
    
    for v in range(len(key)):
        if not mst_set[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v
    
    return min_index 


graph = [[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]

prim_mst(graph)