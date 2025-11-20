class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        out = 0
        for i in range(len(words)):
            found = True
            split = []
            split = [c for c in words[i]]
            for val in split:
                if val not in allowed:
                    found = False
            out += 1 if found else 0
        return out