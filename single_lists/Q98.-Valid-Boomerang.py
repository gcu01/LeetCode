class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # optimization
        
        # 1. Check distinct
        if len(set(map(tuple, points))) < 3:
            return False
        (x1, y1), (x2, y2), (x3, y3) = points

        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)

        # my version - is not working
        '''
        if len(points) < 3:
            return False            
        
        dx = -1
        dx = -1
        for i in range(1, len(points)):
            print(abs(points[i][0]-points[i-1][0]))
            print(abs(points[i][1]-points[i-1][1]))
            print(points[i][0] != points[i-1][0])
            print(points[i][1] != points[i-1][1])
            print("----------------------")
            if dx == -1:
                dx = abs(points[1][0]-points[0][0])
                dy = abs(points[1][1]-points[0][1])
                if points[i][0] == points[i-1][0] and points[i][1] == points[i-1][1]:
                    return False
            if (abs(points[i][0]-points[i-1][0]) != dx or abs(points[i][1]-points[i-1][1]) != dy) and (points[i][0] != points[i-1][0] or points[i][1] != points[i-1][1]):
                return True
        return False
        '''