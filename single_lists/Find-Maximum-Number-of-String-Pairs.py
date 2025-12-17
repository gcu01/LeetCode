1class Solution(object):
2    def maximumNumberOfStringPairs(self, words):
3        """
4        :type words: List[str]
5        :rtype: int
6        """
7        res = 0
8        #print(words[0][::-1])
9        while len(words):
10            if words[0][::-1] in words and 0 != words.index(words[0][::-1]):
11                res += 1
12                #print("before words=", words)
13                words.remove(words[0][::-1])
14                #print("after words=", words)
15
16            words.remove(words[0])
17        return res