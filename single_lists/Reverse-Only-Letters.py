1class Solution(object):
2    def reverseOnlyLetters(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        ls = list(s)
8        i, j = 0, len(s)-1
9        while i<j:
10            if ls[i].isalpha() and ls[j].isalpha():
11                ls[i], ls[j] = ls[j], ls[i]
12                i += 1
13                j -= 1
14            elif ls[i].isalpha() == False:
15                i += 1
16            else:
17                j -= 1
18        s = "".join(ls)
19        return s
20            
21
22