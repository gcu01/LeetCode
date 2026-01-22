1class Solution(object):
2    def stableMountains(self, height, threshold):
3        """
4        :type height: List[int]
5        :type threshold: int
6        :rtype: List[int]
7        """
8        out = []
9        for i in range(1, len(height)):
10            if height[i-1] > threshold:
11                out.append(i)
12        return out