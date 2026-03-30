1class Solution(object):
2    def minimumCost(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        nums[1:] = sorted(nums[1:])
8        return sum(nums[:3])
9
10
11        
12        ns = sorted(nums)
13        s = 0
14        if nums[0] not in [ns[0],ns[1]]:
15                return nums[0] + ns[0] + ns[1]                
16        
17        idx0 = nums.index(ns[0])
18        idx1 = nums.index(ns[1])
19        print("idx0=", idx0, "    idx1=", idx1)
20        return ns[0] + ns[1] + nums[max(idx0, idx1) + 1]
21