1class Solution(object):
2    def maximizeExpressionOfThree(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        #optimized solution
8        nums.sort()
9        return (nums[-1]+nums[-2]-nums[0])
10
11        #my solution - not efficient
12        maxim = 0
13        for i in range(len(nums)):
14            a = nums[i]
15            for j in range(i+1, len(nums)):
16                b = nums[j]
17                for k in range(j+1, len(nums)):
18                    c = nums[k]
19                    if (a + b -c) > maxim:
20                        maxim = a + b -c
21                        print("maxim = ", maxim)
22        return maxim