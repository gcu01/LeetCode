class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start>destination:
            start, destination = destination, start
        sum1= sum(distance[start:destination]) 
        #print(sum1)
        sum2= sum(distance[0:start]) + sum(distance[destination:]) #+ distance[-1]
        #print(sum(distance[0:start]))
        #print(sum(distance[destination:]))
        #print(distance[-1])
        #print(sum2)
        return min(sum1, sum2)