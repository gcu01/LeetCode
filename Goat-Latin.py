1class Solution(object):
2    def toGoatLatin(self, sentence):
3        """
4        :type sentence: str
5        :rtype: str
6        """
7        sentence = sentence.split(" ")
8        for i in range(len(sentence)):
9            #print("first letter=", sentence[i][0])
10            if sentence[i][0].lower() in "aeiou":
11                sentence[i] = sentence[i] + "ma"
12            else:
13                sentence[i] = sentence[i][1:] + sentence[i][0] + "ma"
14            sentence[i] = sentence[i] + "a"*(i+1)
15        return " ".join(sentence)
16            