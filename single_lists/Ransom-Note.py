1class Solution(object):
2    def canConstruct(self, ransomNote, magazine):
3        """
4        :type ransomNote: str
5        :type magazine: str
6        :rtype: bool
7        """
8        if len(magazine) < len(ransomNote):
9            return False
10        ml = list(magazine)
11        for val in ransomNote:
12            if val not in ml:
13                return False
14            ml.remove(val)
15
16        return True