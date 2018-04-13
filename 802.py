class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """    
        def build_rev(graph):
            rev = [[] for i in range(len(graph))]
            for i, edges in enumerate(graph):
                for j, edge in enumerate(edges):
                    rev[edge].append(i)
            return rev

        def dfs(graph,rev,vis,i):
            vis[i] = True
            for edge in graph[i]:
                if vis[edge] == False:
                    dfs(graph,rev,vis,edge)
            if len(graph[i])== 0:
                for edge in rev[i]:
                    graph[edge].remove(i)
                    dfs(graph,rev,vis,edge)
                rev[i] = []

        rev = build_rev(graph)
        vis = [False]*len(graph)
        save = []
        
        for i in range(len(graph)):
            dfs(graph,rev,vis,i)
            if len(graph[i]) == 0:
                save.append(i)
                
        return save