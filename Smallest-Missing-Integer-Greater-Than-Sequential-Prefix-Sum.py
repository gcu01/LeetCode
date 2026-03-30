1class Solution(object):
2    def missingInteger(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n = len(nums)
8        if n==1:
9            return nums[0]+1
10        s = nums[0]
11        nr = 1
12        d = []
13        for i in range(1, n):
14            if nums[i-1]+1 == nums[i]:
15                s += nums[i]
16                nr += 1
17                if i == n-1:
18                    d.append([nr,s])
19            else:
20                if nr>1:
21                    d.append([nr,s])
22                s = nums[i]
23                nr = 1
24        if d == []:
25            d.append([1,max(nums)])
26        #print(d)
27        d.sort(key=lambda x:x[0], reverse = True)
28        #print(d)
29        out = d[0][1] 
30        while True:
31            if out in nums:
32                out += 1
33            else:
34                break
35        return out
36
37
38        