1class Solution(object):
2    def leftRightDifference(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        leftSum = [0]*(len(nums))
8        rightSum = [0]*(len(nums))
9        out = [0]*(len(nums))
10        #print(len(leftSum))
11        for i in range(len(nums)):
12            #print("i=", i)
13            leftSum[i] = sum(nums[:i])
14            rightSum[i] = sum(nums[i+1:])
15            out[i] = abs(leftSum[i] - rightSum[i])
16        #print("leftSum=", leftSum)
17        #print("rightSum=", rightSum)
18        return out
19
20