1class Solution(object):
2
3    def sumDigits(self, val):
4        if val < 10:
5            return val
6        s = 0
7        remainder = 0
8        while val:
9            remainder = val%10
10            val = val/10
11            s += remainder
12        return s
13
14    def minElement(self, nums):
15        """
16        :type nums: List[int]
17        :rtype: int
18        """
19        for i in range(len(nums)):
20            #print("val =", nums[i], "   sumDigits=", self.sumDigits(nums[i]))
21            nums[i] = self.sumDigits(nums[i])
22        return min(nums)
23        