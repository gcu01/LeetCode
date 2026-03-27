1class Solution(object):
2    def largestPerimeter(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        nums.sort(reverse = True)
8        #print(nums)
9        
10        for i in range(len(nums)-2):
11            if nums[i] < nums[i+1]+nums[i+2]:
12                return nums[i]+nums[i+1]+nums[i+2]
13        return 0
14        '''
15        for i in range(len(nums)):
16            for j in range(i+1, len(nums)):
17                for k in range(j+1, len(nums)):
18                    val1, val2, val3 = nums[i], nums[j], nums[k]                    
19                    if val3+val2>val1:
20                        return val1+val2+val3
21        return 0
22        '''
23        