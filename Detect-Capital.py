1class Solution(object):
2    def detectCapitalUse(self, word):
3        """
4        :type word: str
5        :rtype: bool
6        """
7        if word.isupper() or word.islower():
8            return True
9        elif word[0].isupper() and word[1:].islower():
10            return True
11        return False