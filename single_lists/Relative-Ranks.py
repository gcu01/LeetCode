class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        if score == []: return []
        places = {}
        order_list = list(score)
        order_list.sort(reverse=True)
        #print(order_list)
        out = []

        for i in range(len(order_list)):
            if i == 0: places[order_list[i]] = "Gold Medal"
            elif i == 1: places[order_list[i]] = "Silver Medal"
            elif i == 2: places[order_list[i]] = "Bronze Medal"
            else: places[order_list[i]] = str(i+1)
        #print(places)
        
        for i in range(len(score)):
            out.append(places[score[i]])
        
        return out