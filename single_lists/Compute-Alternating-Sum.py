1class Solution(object):
2    def alternatingSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        s1 = sum(nums[::2])
8        s2 = sum(nums)-s1
9        #print("s1=", s1, "   s2=", s2)
10        return s1-s2