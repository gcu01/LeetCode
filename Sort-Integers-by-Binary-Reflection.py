1import sys
2
3class Solution(object):
4    def sortByReflection(self, nums):
5        """
6        :type nums: List[int]
7        :rtype: List[int]
8        """
9        out = []
10        n = len(nums)
11        for i in range(n):
12            b = str(bin(nums[i])[2:])
13            #print(b)
14            s1 = b[::-1]
15            #print(s1)
16            bb = int(s1, 2)
17            #print(bb)
18            out.append([nums[i], bb])
19        #print(out)
20        out.sort(key = lambda x: x[0])
21        out.sort(key = lambda x: x[1])
22        #print(out)
23        return [x for [x,y] in out]
24        
25