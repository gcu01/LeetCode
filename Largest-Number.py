1class Solution(object):
2    def largestNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: str
6        """
7        numstr = [str(x) for x in nums]
8        #print(numstr)
9        numstr.sort(key = lambda a:a*10, reverse = True)
10        #print(numstr)
11        if numstr[0] == "0":
12            return "0"
13        return "".join(numstr)
14        