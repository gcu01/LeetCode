1class Solution(object):
2    def minOperations(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        nums.sort()
9        op = 0
10        for i in range(len(nums)):
11            if nums[i] < k:
12                op += 1
13            else:
14                return op
15        return op