1class Solution(object):
2    def maxOperations(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        op = 0
8        s = 0
9        if len(nums) < 2:
10            return op
11
12        op += 1
13        s = nums[0] + nums[1]        
14        del nums[0:2]
15
16        while len(nums) > 1:
17            if nums[0]+nums[1] == s:
18                del nums[0:2]
19                op += 1
20            else:
21                break
22                
23        return op
24