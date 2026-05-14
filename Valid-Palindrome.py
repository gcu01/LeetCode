1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        s = s.lower()
8        #print("lower s =", s)
9        s = "".join(x for x in s if x.isalpha() or x.isdigit())
10        #print("s =", s)
11
12        i, j = 0, len(s)-1
13        while i < j:
14            if s[i] != s[j]:
15                return False
16            i += 1
17            j -= 1
18        return True