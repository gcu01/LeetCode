1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        n = len(s)-1
8        i, j = 0, n
9        #print("initial i=", i, "   j=", j)
10        #print("test=", s[0].upper())
11        while i < j:
12            if s[i].isalnum() == False:
13                #print("not alpha i = ", s[i])
14                i += 1
15                #if i>=j and j == n:
16                #    return False
17                continue
18            if s[j].isalnum() == False:                
19                j -= 1
20                #if i>=j and i == 0:
21                #    return False
22                continue
23            if s[i].upper() != s[j].upper():
24                #print("i=", i, "first=",s[i].upper(), "     j=", j, "    second=", s[j].upper())
25                return False          
26            i += 1
27            j -= 1
28        return True