1class Solution(object):
2    def zigzagTraversal(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: List[int]
6        """
7        out = []
8        #line = []
9        for i, row in enumerate(grid):
10            #print(row)
11            if i%2 == 0:
12                out += row
13            else:
14                out += row[::-1]
15        #print(out)
16        return out[::2]
17
18        '''
19        for i in range(len(grid)):
20            line = []
21            for j in range(len(grid[0])):
22                if i%2 == 0:
23                    if j%2 == 0:
24                        line.append(grid[i][j])
25                else:
26                    if j%2 != 0:
27                        line.append(grid[i][j])
28            if i%2 != 0:
29                line.reverse()
30            out += line
31        '''
32        return out   
33