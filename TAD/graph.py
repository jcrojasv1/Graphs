from algorithms import dfs as dfs


class Graph:
    def __init__(self,directed,cmp_funct):
        """
        Initializationg for an empty graph

        Args:
            directed (bool): Whether or  not the graph is directed or not 
            cmp_funct (function): Comparation function for comparing two verteces.
        """
        self.directed = directed
        self.cmp_function = cmp_funct
        self.verteces = {}
        self.edges = {}        
        
    def addVertex(self, v, info=None):
        """
        Adds a vertex to the graph

        Args:
            v (int,float,str): Keys for the vertex
            info (any, optional): Information for the graph. Defaults to None.
        """
        self.verteces[v] = info
    
    def addEdge(self,v1,v2,weight=0.0):
        """
        Makes a connection between v1 and v2

        Args:
            v1 (str): _description_
            v2 (str): _description_
            weight (float, optional): _description_. Defaults to 0.
        """
        
        if self.edges.get(v1,None) == None:
            self.edges[v1] = {}
        self.edges[v1][v2] = weight
        
        if not self.directed:
            if self.edges.get(v2,None) == None:
                self.edges[v2] = {}
            self.edges[v2][v1] = weight
        
    def deleteVertex(self,v):
        self.verteces.pop(v)
        
    def DFS(self,init):
        dfs.dfs(self,init)
        path = dfs.dfs(self,init)
        
        return path