1class Solution(object):
2    def heightChecker(self, heights):
3        """
4        :type heights: List[int]
5        :rtype: int
6        """
7        h_ord = sorted(heights)
8        out = 0
9        for i in range(len(heights)):
10            if heights[i] != h_ord[i]:
11                out += 1
12        return out