1class Solution(object):
2    def countSubarrays(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        out = 0
8        if len(nums)<3:
9            return out
10        for i in range(2, len(nums)):
11            #print(nums[i-2]+nums[i])
12            #print(-7/2.0)
13            if 2*(nums[i-2]+nums[i]) == (nums[i-1]):
14                out += 1
15        return out