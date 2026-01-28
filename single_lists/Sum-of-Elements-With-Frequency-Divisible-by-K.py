1class Solution(object):
2    def sumDivisibleByK(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        s = 0
9        lst = []
10        for val in nums:
11            if nums.count(val) % k == 0 and val not in lst:
12                lst.append(val)
13                s += val * nums.count(val)
14        return s