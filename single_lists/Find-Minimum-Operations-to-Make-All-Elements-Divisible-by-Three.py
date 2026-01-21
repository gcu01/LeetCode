1class Solution(object):
2    def minimumOperations(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        out = 0
8        for val in nums:
9            if val % 3 != 0:
10                if (val%3)<2: 
11                    out += 1
12                else:
13                    out += 3 - val%3
14                #print("out += ", 3 - val%3)
15        return out