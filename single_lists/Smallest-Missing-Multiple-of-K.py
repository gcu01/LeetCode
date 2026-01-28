1class Solution(object):
2    def missingMultiple(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        multiple = 1
9        
10        while True:
11            if k * multiple not in nums:
12                return k * multiple
13            multiple += 1
14        return ""