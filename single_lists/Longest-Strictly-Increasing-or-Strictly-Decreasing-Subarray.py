1class Solution(object):
2    def longestMonotonicSubarray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        increase, decrease, dummy_inc, dummy_dec = 0, 0, 0, 0
8        
9        for i in range(1, len(nums)):
10            if nums[i-1] > nums[i]:
11                #print("incr nums[i-1] =", nums[i-1], "  nums[i]=", nums[i])
12                dummy_inc += 1
13                if dummy_inc > increase:
14                    increase = dummy_inc 
15            else:
16                dummy_inc = 0
17            if nums[i-1] < nums[i]:
18                #print("decr nums[i-1] =", nums[i-1], "  nums[i]=", nums[i])
19                dummy_dec += 1
20                if dummy_dec > decrease:
21                    decrease = dummy_dec
22            else:
23                dummy_dec = 0
24        #print("incr=", increase, "   decr=", decrease)
25        return increase+1 if increase > decrease else decrease+1