1class Solution(object):
2    def vowelStrings(self, words, left, right):
3        """
4        :type words: List[str]
5        :type left: int
6        :type right: int
7        :rtype: int
8        """
9        out = 0
10        vowels = "aeiou"
11        for val in words[left: right+1]:
12            if val[0] in vowels and val[len(val)-1] in vowels:
13                out += 1
14        return out