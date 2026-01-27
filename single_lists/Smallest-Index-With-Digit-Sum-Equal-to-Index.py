1class Solution(object):
2    def sumDigits(self, val):
3        s = 0
4        if val < 10:
5            return val
6        else:
7            while val >= 10:
8                s += val%10
9                val /= 10
10            s += val
11        #print("s=", s)
12        return s
13
14    def smallestIndex(self, nums):
15        """
16        :type nums: List[int]
17        :rtype: int
18        """
19        for i, val in enumerate(nums):
20           # print("i = ", i, "  val=", val, "  sumDigits=", self.sumDigits(val))
21            if i == self.sumDigits(val):
22                return i
23        return -1