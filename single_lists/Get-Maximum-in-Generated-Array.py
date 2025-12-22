1class Solution(object):
2    def getMaximumGenerated(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        if n == 0:
8            return 0
9        nums = [0] * (n+1)
10        nums[0] = 0
11        nums[1] = 1
12        #nums[2] = 1
13        for i in range(2, n+1):
14            if i%2 == 0:
15                nums[i] = nums[i/2]
16            else:
17                nums[i] = nums[(i-1)/2] + nums[((i-1)/2) + 1]
18        #print(nums)
19        return max(nums)
20        