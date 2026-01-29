1class Solution(object):
2    def strStr(self, haystack, needle):
3        """
4        :type haystack: str
5        :type needle: str
6        :rtype: int
7        """
8        for i, val in enumerate(haystack):
9            if needle == haystack[i: i+len(needle)]:
10                return i
11        
12        #len_needle = len(needle)
13        #while i < len(haystack):
14        #    if need
15        #    i += 1
16
17
18
19        return -1