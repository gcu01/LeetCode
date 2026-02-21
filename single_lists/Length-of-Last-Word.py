1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        s_words = s.split()
8        return len(s_words[-1])