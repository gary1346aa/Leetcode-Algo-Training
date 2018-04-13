class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        vmax = []
        hmax = []
        for i in range(len(grid)):
            tmp = -1
            for j in range(len(grid[i])):
                if grid[i][j] > tmp:
                    tmp = grid[i][j]
            hmax.append([tmp,i])

        for j in range(len(grid[0])):
            tmp = -1
            for i in range(len(grid)):
                if grid[i][j] > tmp:
                    tmp = grid[i][j]
            vmax.append([tmp,j])

        gridNew = [[101 for j in range(len(grid[i]))] for j in range(len(grid))]

        for h in sorted(hmax, reverse = True):
            for j in range(len(grid[0])):
                gridNew[h[1]][j] = min(gridNew[h[1]][j],h[0])


        for v in sorted(vmax, reverse = True):
            for i in range(len(grid)):
                gridNew[i][v[1]] = min(gridNew[i][v[1]],v[0])

        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                s += gridNew[i][j] - grid[i][j]

        return s