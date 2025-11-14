class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuf = dict()
        for i in range(len(s)):
            shuf[indices[i]]=s[i]
        shuf = {k: shuf[k] for k in sorted(shuf)}        
        return "".join((list(shuf.values())))