1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8        k = 0
9        ln = len(nums)
10        idx = ln-1
11        i = 0
12        while i <= idx:
13            if nums[i] == val:
14                nums[i], nums[idx] = nums[idx], nums[i]
15                idx -= 1
16            else:
17                i += 1
18        return idx+1 
19
20
21
22
23
24        for i in range(len(nums)):
25            if nums[i] == val:
26                while nums[idx] == val:
27                    idx -= 1
28                    k += 1
29                    print("new idx = ", idx)
30                nums[i], nums[idx] = nums[idx], nums[i]
31
32        print("k=",k,"  ln-k=",ln-k)
33        print("nums=", nums)
34        return ln-k