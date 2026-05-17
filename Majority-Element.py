1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        d = dict()
8        for val in nums:
9            d[val] = d.get(val, 0) + 1
10        
11        ln = len(nums) / 2
12
13        for key, val in d.items():
14            if val > ln:
15                return key