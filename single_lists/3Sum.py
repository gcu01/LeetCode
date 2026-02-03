1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        out = []
8        t = []
9        for i in range(len(nums)):
10            for j in range(i+1,len(nums)):
11                for k in range(j+1,len(nums)):
12                    if nums[i]+nums[j]+nums[k] == 0:                   
13                        t = [nums[i], nums[j], nums[k]] 
14                        t.sort()
15                        #print(t)
16                        if t not in out:
17                            out.append(t)
18        return out