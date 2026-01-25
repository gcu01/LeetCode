1class Solution(object):
2    def countPartitions(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        out = 0
8        total = sum(nums)
9        #print(total)
10        left = 0
11        for i in range(1,len(nums)):
12            #if (sum(nums[0:i+1])-sum(nums[i+1:]))%2 == 0:
13            #    out += 1
14            left += nums[i-1]
15            #print("left=", left)
16            if ((total - left)-left)%2 == 0:
17                out += 1
18        return out
19