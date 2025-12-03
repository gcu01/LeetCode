1class Solution(object):
2    def arithmeticTriplets(self, nums, diff):
3        """
4        :type nums: List[int]
5        :type diff: int
6        :rtype: int
7        """
8        triplets = 0
9        for i in range(len(nums)):
10            if (nums[i] + diff) in nums[i+1:] and (nums[i] + diff*2) in nums[nums.index(nums[i]+diff)+1:]:
11                triplets += 1 
12        return triplets