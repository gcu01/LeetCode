1class Solution(object):
2    def isPrefixOfWord(self, sentence, searchWord):
3        """
4        :type sentence: str
5        :type searchWord: str
6        :rtype: int
7        """
8        lst = sentence.split(" ")
9        print(lst)
10        out = 0
11        for i, val in enumerate(lst):
12            if len(val) >= len(searchWord) and searchWord == val[0:len(searchWord)]:
13                return i+1
14        return -1