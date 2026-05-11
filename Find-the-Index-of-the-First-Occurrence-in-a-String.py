1class Solution(object):
2    def strStr(self, haystack, needle):
3        """
4        :type haystack: str
5        :type needle: str
6        :rtype: int
7        """
8        for i in range(len(haystack)-len(needle)+1):
9            if haystack[i:i+len(needle)] == needle:
10                return i            
11        return -1
12