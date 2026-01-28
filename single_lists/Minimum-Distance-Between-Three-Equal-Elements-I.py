1class Solution(object):
2    def minimumDistance(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        minim = float('inf')
8        for i in range(len(nums)):
9            for j in range(i+1, len(nums)):
10                for k in range(j+1, len(nums)):
11                    if nums[i] == nums[j] and nums[j] == nums[k]:
12                        if (abs(i-j) + abs(j-k) + abs(k-i)) < minim:
13                            minim = abs(i-j) + abs(j-k) + abs(k-i)
14        return minim if minim != float('inf') else -1