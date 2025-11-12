class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        #print(words)
        out=[]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    #print("words[i]=", words[i])
                    #print("words[j]=", words[j])
                    out.append(words[i])
                    break
        return out