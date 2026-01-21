1class Solution(object):
2    def satisfiesConditions(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: bool
6        """
7        for i in range(len(grid)):
8            for j in range(len(grid[0])):
9                #print("grid[i][j] =", grid[i][j]), "    grid[i-1][j]=", grid[i-1][j], "   grid[i][j-1]=", grid[i][j-1])
10                if i < len(grid)-1 and grid[i][j] != grid[i+1][j]:
11                    return False
12                if j < len(grid[0])-1 and grid[i][j] == grid[i][j+1]:
13                    return False
14        return True