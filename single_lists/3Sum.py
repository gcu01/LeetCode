1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        nums.sort()
8        n = len(nums)
9        out = []
10        for i in range(n):
11            if i > 0 and nums[i] == nums[i-1]:
12                continue
13            left, right = i+1, n-1
14            while left < right:
15                total = nums[i] + nums[left] + nums[right]
16
17                if total == 0:
18                    out.append([nums[i], nums[left], nums[right]])
19                
20                    while left < right and nums[left] == nums[left+1]:
21                        left += 1
22                    while left < right and nums[right] == nums[right-1]:
23                        right -= 1
24                    
25                    left += 1
26                    right -= 1
27                elif total < 0:
28                    left += 1
29                else:
30                    right -= 1
31        return out
32
33                
34
35
36        # brute force - not feasible for large amount of input
37        '''
38        out = []
39        t = []
40        for i in range(len(nums)):
41            for j in range(i+1,len(nums)):
42                for k in range(j+1,len(nums)):
43                    if nums[i]+nums[j]+nums[k] == 0:                   
44                        t = [nums[i], nums[j], nums[k]] 
45                        t.sort()
46                        #print(t)
47                        if t not in out:
48                            out.append(t)
49        return out
50        '''