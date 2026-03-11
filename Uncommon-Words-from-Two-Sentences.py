1class Solution(object):
2    def uncommonFromSentences(self, s1, s2):
3        """
4        :type s1: str
5        :type s2: str
6        :rtype: List[str]
7        """
8        if s1 == "":
9            return s2.split(" ")
10        elif s2 == "":
11            return s1.split(" ")
12        s1_lst = s1.split(" ")
13        s2_lst = s2.split(" ")
14        s = s1_lst + s2_lst
15        out = []
16        for val in s:
17            if s.count(val) == 1:
18                out.append(val)
19        return out