1class Solution(object):
2    def smallestAbsent(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7
8        avg = sum(nums)/len(nums)
9        #print("avg=", avg)
10        nums = [x for x in nums if x > avg and x > 0]
11        #print("nums=", nums)
12        if nums == []:
13            return avg+1 if avg>0 else 1
14        
15        maximum = max(nums)
16        l0 = avg+1 if avg>=0 else 1
17        lst = range(l0,maximum+2)
18        for val in lst:
19            if val not in nums:
20                return val                
21        return 0
22