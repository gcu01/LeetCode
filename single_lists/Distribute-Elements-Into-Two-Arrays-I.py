1class Solution(object):
2    def resultArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        n1, n2 = [], []
8        n1.append(nums[0])
9        n2.append(nums[1])
10
11        for i in range(2, len(nums)):
12            if n1[-1] > n2[-1]:
13                n1.append(nums[i])
14            else:
15                n2.append(nums[i])
16        #print("n1=", n1)
17        #print("n2=", n2)
18        return n1+n2
19