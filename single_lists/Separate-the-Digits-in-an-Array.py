1class Solution(object):
2    def separateDigits(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        out = []
8        for val in nums:
9            if val<10:
10                out.append(val)
11            else:
12                i = 0
13                while val:
14                    out.insert(len(out)-i, val%10)
15                    i += 1
16                    val //= 10
17        return out