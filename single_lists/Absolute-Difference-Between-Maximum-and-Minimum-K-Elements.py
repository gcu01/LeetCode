1class Solution(object):
2    def absDifference(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        nums.sort()
9        n = len(nums)
10        sum_largest = sum(nums[n-k:])
11        sum_smallest = sum(nums[:k])
12        return abs(sum_largest-sum_smallest)