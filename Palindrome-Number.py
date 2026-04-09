1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7        if x < 0:
8            return False
9        x_str = str(x)
10        rev_x_str = x_str[::-1]
11        if x_str == rev_x_str:
12            return True
13        return False