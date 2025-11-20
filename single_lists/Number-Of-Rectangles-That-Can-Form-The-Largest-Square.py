class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxim = 0
        out = []
        for i in range(len(rectangles)):
            minim = min(rectangles[i])
            out.append(minim)
            #print("minim=",minim)
            #if maxim < minim:
            #    maxim = minim
            #    out.append
            #print("maxim=",maxim)
        maxim = max(out)
        return out.count(maxim)
        #return maxim
        