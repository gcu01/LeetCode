class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        out = 0
        if ruleKey == "type":
            for i in range(len(items)):
                if ruleValue == items[i][0]:
                    out+=1
            return out
        elif ruleKey == "color":
            for i in range(len(items)):
                if ruleValue == items[i][1]:
                    out+=1
            return out            
        else:
            for i in range(len(items)):
                if ruleValue == items[i][2]:
                    out+=1
            return out
        return ""