1class Solution(object):
2    def findMissingElements(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        maxim = max(nums)
8        minim = min(nums)
9        perfect = range(minim, maxim+1)
10        out = []
11        for val in perfect:
12            if val not in nums:
13                out.append(val)
14        return out