class Solution:
    
    def dfs(graph, path, i):
        if graph[i] == []:
            return [path]
        else:
            paths = []
            for element in graph[i]:
                paths += Solution.dfs(graph, path + [element], element)
            return paths
        
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        return Solution.dfs(graph,[0], 0)