1class Solution(object):
2    def minimumOperations(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        n = len(grid[0])
8        out = []
9
10        for i in range(1, len(grid)):
11            for j in range(n):
12                #print("grid[i][j]=", grid[i][j])
13                if grid[i][j] <= grid[i-1][j]:
14                    #print("before grid[i][j]=", grid[i][j], "   grid = ", grid)
15                    out.append(abs(grid[i][j] - grid[i-1][j]) +1)
16                    grid[i][j] += abs(grid[i][j] - grid[i-1][j]) +1
17                    #print("after gris[i][j]=", grid[i][j], "   grid = ", grid)
18                    #print("------------")
19        #print("out=", out)
20        return sum(out)
21                