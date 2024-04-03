
from collections import deque


class Graph:
    def __init__(self, edges, n) -> None:
        self.edges = edges 
        self.node = n
        
        self.adjList = [ [] for i in range(self.node)]
        
        for (src, dest) in self.edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            
    
    def bfs(self, v, discorved):
        q = deque()
        
        discorved[v] = True 
        
        
        q.append(v)
        
        while q: 
            v = q.popleft()
            print(v, end='')
            
            for u in self.adjList(v):
                if not discorved[u]:
                    discorved[u] = True
                    q.append(u)
        
        
        
