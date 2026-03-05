1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        words = s.split(" ")
8        #print(words)
9        for i in range(len(words)):
10            words[i] = words[i][::-1]
11        #print(words)
12        return " ".join(words)
13        '''
14        k = 0
15        dummy = ""
16        out = ""
17        for i in range(len(s)):
18            if s[i]==" ":
19                #print(s[k:i][::-1])
20                out += s[k:i][::-1] + " "
21                k = i+1
22        dummy = s[k:][::-1]
23        out += dummy
24        return out
25        '''