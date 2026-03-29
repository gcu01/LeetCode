1class Solution(object):
2    def minimumDifference(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        n = len(nums)
9        nums.sort()
10        #print("sorted nums=", nums)
11        mn = nums[k - 1] - nums[0]       
12        for i in range(0, n-k+1):
13            mn = min(nums[i+k-1]-nums[i], mn)
14        return mn
15                