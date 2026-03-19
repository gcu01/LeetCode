1class Solution(object):
2    def isPalindrom(self, s):
3        start, end = 0, len(s)-1
4        while start < end:
5            if s[start] != s[end]:
6                return False
7            start += 1
8            end -= 1
9        return True
10    def validPalindrome(self, s):
11        """
12        :type s: str
13        :rtype: bool
14        """
15        s_lst = list(s)
16        i, j = 0, len(s_lst)-1
17        while i<j:
18            if s_lst[i] == s_lst[j]:
19                i += 1
20                j -= 1
21            else:
22                if self.isPalindrom(s[i+1:j+1]):
23                    return True
24                elif self.isPalindrom(s[i:j]):
25                    return True
26                return False
27        return True