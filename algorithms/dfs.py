"""
DFS (Depth-first search) Algorithm for the class Graph.
    
"""



marked = []
print(marked)

def dfs(graph,init):
    if not init in marked:
        marked.append(init)
        for vertex in list(graph.edges[init]):
            dfs(graph,vertex)
    return marked