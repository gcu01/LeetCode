1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        seen = dict()
9        for i, val in enumerate(nums):
10            #print("target-val=", target-val)
11            if target - val in seen.values():
12                for k, v in seen.items():
13                    if v == target-val:
14                        return [k, i]
15            else:
16                seen[i] = val
17                #print("seen=", seen.items())
18            
19        