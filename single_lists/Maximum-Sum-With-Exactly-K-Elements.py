1class Solution(object):
2    def maximizeSum(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        # improved 1
9        s = 0
10        #return max(nums)*k +k if k> 2 else max(nums)*k +1
11        m = max(nums)
12        while k:            
13            s += m
14            m += 1
15            k -= 1
16        return s
17        # version 1
18        '''
19        s = 0
20        while k:
21            m = max(nums)
22            idx = nums.index(m)
23            s += m
24            nums[idx] = m+1
25            k -=1
26        return s
27        '''