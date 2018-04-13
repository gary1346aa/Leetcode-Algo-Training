class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        s = abs(target[0]) + abs(target[1])
        for g in ghosts:
            if abs(target[0] - g[0])+ abs(target[1] - g[1]) <= s:
                return False
            
        return True