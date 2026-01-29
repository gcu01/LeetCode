1class Solution(object):
2    def reverseSubmatrix(self, grid, x, y, k):
3        """
4        :type grid: List[List[int]]
5        :type x: int
6        :type y: int
7        :type k: int
8        :rtype: List[List[int]]
9        """
10        top, bottom = x, x+k-1
11
12        while top<bottom:
13            for j in range(k):
14                grid[top][y+j], grid[bottom][y+j]  = grid[bottom][y+j], grid[top][y+j]
15            top += 1
16            bottom -= 1
17        return grid
18