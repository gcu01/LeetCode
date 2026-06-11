1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8        idx = 0
9        n = len(nums) - 1
10        while idx <= n:
11            if nums[idx] == val:
12                #nums[idx], nums[n] = nums[n], nums[idx]
13                nums.pop(idx)
14                n -= 1
15            else:
16                idx += 1
17        #print("nums = ", nums)
18        #print("n=", n)
19        #nums = nums[:n+1]
20        return len(nums)
21
22
23
24
25
26
27
28
29
30
31
32        k = 0
33        ln = len(nums)
34        idx = ln-1
35        i = 0
36        while i <= idx:
37            if nums[i] == val:
38                nums[i], nums[idx] = nums[idx], nums[i]
39                idx -= 1
40            else:
41                i += 1
42        return idx+1 