1class Solution(object):
2    def smallerNumbersThanCurrent(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        d = dict()
8        out = [0]*len(nums)
9        for i, val in enumerate(nums):
10            d[i] = val
11        #print("dict=",d)
12        nums.sort()
13        #print(nums)
14        for i in range(len(nums)):
15            out[i] = nums.index(d[i])
16        return out
17
18
19
20
21        '''
22        #s = nums
23        #s.sort(reverse = True)
24        n = len(nums)
25        out = [0]*len(nums)
26        #print(out)
27        while len(nums)>0:
28            m = max(nums)
29            c = nums.count(m)
30            idx = nums.index(m)           
31            out[idx] = n-c
32            del nums[idx]
33            print("max= ",m, "count= ", c, "index =", idx)
34            print(" nums = ", nums)
35            print("out = ", out)
36        #print(out)
37        return out
38        '''