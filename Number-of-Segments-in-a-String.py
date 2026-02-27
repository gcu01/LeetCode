1class Solution(object):
2    def countSegments(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        count = 0
8        for i in range(len(s)-1, 0, -1):
9            if s[i] != " " and s[i-1] == " ":
10                count += 1
11        if len(s) and s[0] != " ":
12            count += 1
13        return count