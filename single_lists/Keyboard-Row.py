1class Solution(object):
2    def inString(self, str1, str2):
3        for i in range(len(str1)):
4            if str1[i] not in str2:
5                return False
6        return True
7    def findWords(self, words):
8        """
9        :type words: List[str]
10        :rtype: List[str]
11        """
12        s1 = "qwertyuiop"
13        s2 = "asdfghjkl"
14        s3 = "zxcvbnm"
15        out = []
16        for val in words:
17            if self.inString(val.lower(), s1):
18                out.append(val)
19            elif self.inString(val.lower(), s2):
20                out.append(val)
21            elif self.inString(val.lower(), s3):
22                out.append(val)
23        return out