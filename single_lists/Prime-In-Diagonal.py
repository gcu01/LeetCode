1class Solution(object):
2    def is_prime(self, n):
3        if n <= 1:
4            return False
5        if n <= 3:
6            return True
7        if n % 2 == 0:
8            return False
9
10        i = 3
11        while i * i <= n:
12            if n % i == 0:
13                return False
14            i += 2
15        return True
16
17    def diagonalPrime(self, nums):
18        """
19        :type nums: List[List[int]]
20        :rtype: int
21        """
22        maxim = -999999
23        for i in range(len(nums)):
24            if self.is_prime(nums[i][i]) and maxim < nums[i][i]:
25                maxim = nums[i][i]
26            if self.is_prime(nums[i][len(nums)-i-1]) and maxim < nums[i][len(nums)-i-1]:
27                maxim = nums[i][len(nums)-i-1]
28        return maxim if maxim != -999999 else 0