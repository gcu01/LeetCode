1class Solution(object):
2    def unequalTriplets(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        out = 0
8        for i in range(len(nums)):
9            for j in range(i+1, len(nums)):
10                for k in range(j+1, len(nums)):
11                    if nums[i] != nums[j] and nums[i]!= nums[k] and nums[j] != nums[k]:
12                        out += 1                        
13        return out