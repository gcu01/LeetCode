1class Solution(object):
2    def checkRecord(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7#        if len(s)<3:
8#            return True
9        if "LLL" in s or s.count("A")>=2:
10            return False
11        return True