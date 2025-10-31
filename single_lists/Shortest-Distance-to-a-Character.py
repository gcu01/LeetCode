class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        #print(range(len(s)))
        letter = []
        for i in range(len(s)):
            if s[i] == c:
                letter.append(i)
        #print(letter)
        j = 0
        out = []
        for i,val in enumerate(s):
            if i <= letter[j]:
                out.append( min(abs(i-letter[j-1]),abs(i-letter[j])) if j>0 else abs(i-letter[j]))
                #print("i = ", i, "i <= letter[j], j =", j, " append=", min(abs(i-letter[j-1]),abs(i-letter[j])) if j>0 else abs(i-letter[j]))
            else:
                j += 1 if j<(len(letter)-1) else 0
                out.append(min(abs(i-letter[j-1]),abs(i-letter[j])))
                #print("i = ", i, "i > letter[j], j =", j, " append = ", min(abs(i-letter[j-1]),abs(i-letter[j])))
        return out
        