1class Solution(object):
2    def reversePrefix(self, word, ch):
3        """
4        :type word: str
5        :type ch: str
6        :rtype: str
7        """
8        for i in range(len(word)):
9            if ch == word[i]:
10                s = word[:i+1]
11                #print(s)
12                return s[::-1] + word[i+1:]
13        return word
14        